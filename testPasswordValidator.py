# testPasswordValidator.py
#
# Author(s): Victoria Seusankar
# 
# Date: 12/2/25
# 
# This file acts as the tester for the password validator.

import unittest
from passwordValidator import passwordValidator
import os
import secrets
import hashlib

class TestpasswordValidator(unittest.TestCase):
  DEBUG = True
    
  # Valid passwords for positive tests
  VALID_PASS = "SecurePass123" 
  VALID_PASS_MIN = "Minimall"     
  VALID_PASS_MAX = "MaximumPassword1" 

  # Set up the validator instance before each test method
  def setUp(self):
      self.validator = passwordValidator() 


  # Test passwords that should be validated 
  def test_is_valid_positive_cases(self):
      if TestpasswordValidator.DEBUG:
          print("\n Testing isValid Positive Cases: ")

      self.assertTrue(self.validator.isValid(TestpasswordValidator.VALID_PASS), "Should validate a valid password.")
      self.assertTrue(self.validator.isValid(TestpasswordValidator.VALID_PASS_MIN), "Should validate password at minimum length (8).")
      self.assertTrue(self.validator.isValid(TestpasswordValidator.VALID_PASS_MAX), "Should validate password at maximum length (16).")


  # Test passwords that fail due to an incorrect length
  def test_is_valid_negative_length_cases(self):
      if TestpasswordValidator.DEBUG:
        print("\n Testing isValid Negative Length Cases: ")

      # Variable for if the password is too short
      short_pass = "short"
      self.assertFalse(self.validator.isValid(short_pass), "Should fail, password is too short (< 8).")
      
      # Variable for if the password is too long
      long_pass = "ThisIsWayTooLongOfAPassword"
      self.assertFalse(self.validator.isValid(long_pass), "Should fail, password is too long (> 16).")
      
      if TestpasswordValidator.DEBUG:
        print(f"Tested short pass '{short_pass}': {self.validator.isValid(short_pass)}") 
        print(f"Tested long pass '{long_pass}': {self.validator.isValid(long_pass)}") 

  
  # Test passwords that fail due to disallowed characters
  def test_is_valid_negative_character_cases(self):
    if TestpasswordValidator.DEBUG:
      print("\n--- Testing isValid Negative Character Cases ---")

    disallowed_chars = {
      'forward_slash': 'bad/pass12',
      'backslash': 'bad\\pass12',
      'less_than': 'bad<pass12',
      'greater_than': 'bad>pass12',
      'pipe': 'bad|pass12',
      'space': 'bad pass12'
    }
        
    for name, password in disallowed_chars.items():
      with self.subTest(char_name = name):
        self.assertFalse(self.validator.isValid(password), f"Should fail due to disallowed character: {name}") 
        if TestpasswordValidator.DEBUG:
          print(f"Tested pass with {name} ('{password}'): {self.validator.isValid(password)}") 


  # Test invalid input types
  def test_is_valid_edge_cases(self):
      if TestpasswordValidator.DEBUG:
        print("\n Testing isValid Edge Cases (Invalid Input): ")

      self.assertFalse(self.validator.isValid(12345678), "Should fail if input is not a string.")
      self.assertFalse(self.validator.isValid(None), "Should fail if input is None.")
      self.assertFalse(self.validator.isValid(""), "Should fail if input is empty string.")
      
      if TestpasswordValidator.DEBUG:
        print(f"Tested non-string input: {self.validator.isValid(12345678)}") 
        print(f"Tested None input: {self.validator.isValid(None)}") 
        print(f"Tested empty string: {self.validator.isValid('')}")


  # Test to see if the hash method returns the correct type and size
  def test_hash_output_format(self):
    if TestpasswordValidator.DEBUG:
      print("\n Testing Hashing Output Format: ")
          
    hashed, salt = self.validator.hash(TestpasswordValidator.VALID_PASS)
    
    # Check the types
    self.assertIsInstance(hashed, bytes, "Hashed password must be bytes.")
    self.assertIsInstance(salt, bytes, "Salt must be bytes.")
    
    # Check the size
    self.assertEqual(len(hashed), 64, "PBKDF2-HMAC with dklen=64 should be 64 bytes.")
    self.assertEqual(len(salt), 16, "Default salt length should be 16 bytes.")
    
    if TestpasswordValidator.DEBUG:
      print(f"Password: {TestpasswordValidator.VALID_PASS}") 
      print(f"Hash (length {len(hashed)}): {hashed.hex()}") 
      print(f"Salt (length {len(salt)}): {salt.hex()}")


  # Test to see if the same password that is hashed twice creates different hashes due to different salts
  def test_hash_salting_effectiveness(self):
    if TestpasswordValidator.DEBUG:
      print("\n--- Testing Hashing/Salting Effectiveness ---")
  
    hashed1, salt1 = self.validator.hash(TestpasswordValidator.VALID_PASS)
    hashed2, salt2 = self.validator.hash(TestpasswordValidator.VALID_PASS)
      
    # The salts must be different
    self.assertNotEqual(salt1, salt2, "Two randomly generated salts must be different.")
    
    # The resulting hashes must be different since the salts are different
    self.assertNotEqual(hashed1, hashed2, "Same password, different salts must create different hashes.")
      
    if TestpasswordValidator.DEBUG:
      print("Hash 1/Salt 1 generated.") 
      print("Hash 2/Salt 2 generated.") 
      print(f"Are the hashes equal? {hashed1 == hashed2} (Should be False)") 


  # Test for successful password verification
  def test_verify_success(self):
    if TestpasswordValidator.DEBUG:
      print("\n Testing Verification (Success): ")

    hashed, salt = self.validator.hash(TestpasswordValidator.VALID_PASS)
    
    is_correct = self.validator.verify(TestpasswordValidator.VALID_PASS, hashed, salt)
    self.assertTrue(is_correct, "Verification should succeed when the password is correct.")

    if TestpasswordValidator.DEBUG:
      print(f"Verification of '{TestpasswordValidator.VALID_PASS}' is successful: {is_correct}") 


  # Test for unsuccessful password verification
  def test_verify_failure(self):
    if TestpasswordValidator.DEBUG:
      print("\n Testing Verification (Failure): ")

    hashed, salt = self.validator.hash(TestpasswordValidator.VALID_PASS)
    incorrect_password = "NotTheCorrectPassword"
    
    is_incorrect = self.validator.verify(incorrect_password, hashed, salt)
    self.assertFalse(is_incorrect, "Verification should fail when the password is incorrect.")

    if TestpasswordValidator.DEBUG:
      print(f"Attempted verification with '{incorrect_password}' has failed: {not is_incorrect}") 


  # Tests that running the hashing process with the same password and salt multiple times gives the same result every time
  def test_verify_with_known_salt(self):
    if TestpasswordValidator.DEBUG:
      print("\n Testing Verification with Known Salt Consistency: ")
  
    # Create a non-random salt
    known_salt = b'1' * 16 
    
    # Hash 1
    hashed1, salt_used = self.validator.hash(TestpasswordValidator.VALID_PASS, known_salt)
    
    # Hash 2
    hashed2, salt_used = self.validator.hash(TestpasswordValidator.VALID_PASS, known_salt)

    self.assertEqual(hashed1, hashed2, "Hashing the same password with same salt must create an identical hash.")
    
    # Verification using the known salt should still pass
    self.assertTrue(self.validator.verify(TestpasswordValidator.VALID_PASS, hashed1, known_salt), "Verification should succeed when using a pre-defined salt.")
    
    if TestpasswordValidator.DEBUG:
      print(f"Hash 1 and Hash 2 are identical: {hashed1 == hashed2}") 
      print("Verification using identical hash/salt pair has been successful.")


if __name__ == '__main__':
    unittest.main()
