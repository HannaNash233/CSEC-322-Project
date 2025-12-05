# testPasswordValidator.py
#
# Author(s): Victoria Seusankar
# 
# Date: 12/2/25
# 
# This file acts as the tester for the password validator.

import unittest
from passwordValidator import PasswordValidator
import os
import secrets
import hashlib

class TestPasswordValidator(unittest.TestCase):
  DEBUG = True
    
  # Valid passwords for positive tests
  VALID_PASS = "SecurePass123" 
  VALID_PASS_MIN = "Minimall"     
  VALID_PASS_MAX = "MaximumPassword1" 

  # Set up the validator instance before each test method
  def setUp(self):
      self.validator = PasswordValidator()


  # Test passwords that should be validated 
  def test_is_valid_positive_cases(self):
      if TestPasswordValidator.DEBUG:
          print("\n Testing is_valid Positive Cases: ")

      self.assertTrue(self.validator.is_valid(TestPasswordValidator.VALID_PASS), "Should validate a valid password.")
      self.assertTrue(self.validator.is_valid(TestPasswordValidator.VALID_PASS_MIN), "Should validate password at minimum length (8).")
      self.assertTrue(self.validator.is_valid(TestPasswordValidator.VALID_PASS_MAX), "Should validate password at maximum length (16).")


  # Test passwords that fail due to an incorrect length
  def test_is_valid_negative_length_cases(self):
      if TestPasswordValidator.DEBUG:
        print("\n Testing is_valid Negative Length Cases: ")

      # Variable for if the password is too short
      short_pass = "short"
      self.assertFalse(self.validator.is_valid(short_pass), "Should fail, password is too short (< 8).")
      
      # Variable for if the password is too long
      long_pass = "ThisIsWayTooLongOfAPassword"
      self.assertFalse(self.validator.is_valid(long_pass), "Should fail, password is too long (> 16).")
      
      if TestPasswordValidator.DEBUG:
        print("Tested short pass '{short_pass}': {self.validator.is_valid(short_pass)}")
        print("Tested long pass '{long_pass}': {self.validator.is_valid(long_pass)}")

  
  # Test passwords that fail due to disallowed characters
  def test_is_valid_negative_character_cases(self):
    if TestPasswordValidator.DEBUG:
      print("\n--- Testing is_valid Negative Character Cases ---")

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
        self.assertFalse(self.validator.is_valid(password), "Should fail due to disallowed character: {name}")
        if TestPasswordValidator.DEBUG:
          print("Tested pass with {name} ('{password}'): {self.validator.is_valid(password)}")


  # Test invalid input types
  def test_is_valid_edge_cases(self):
      if TestPasswordValidator.DEBUG:
        print("\n Testing is_valid Edge Cases (Invalid Input): ")

      self.assertFalse(self.validator.is_valid(12345678), "Should fail if input is not a string.")
      self.assertFalse(self.validator.is_valid(None), "Should fail if input is None.")
      self.assertFalse(self.validator.is_valid(""), "Should fail if input is empty string.")
      
      if TestPasswordValidator.DEBUG:
        print("Tested non-string input: {self.validator.is_valid(12345678)}")
        print("Tested None input: {self.validator.is_valid(None)}")
        print("Tested empty string: {self.validator.is_valid('')}")


  # Test to see if the hash method returns the correct type and size
  def test_hash_output_format(self):
    if TestPasswordValidator.DEBUG:
      print("\n Testing Hashing Output Format: ")
          
    hashed, salt = self.validator.hash(TestPasswordValidator.VALID_PASS)
    
    # Check the types
    self.assertIsInstance(hashed, bytes, "Hashed password must be bytes.")
    self.assertIsInstance(salt, bytes, "Salt must be bytes.")
    
    # Check the size 
    self.assertEqual(len(hashed), 32, "SHA-256 hash length should be 32 bytes.")
    self.assertEqual(len(salt), 16, "Default salt length should be 16 bytes.")
    
    if TestPasswordValidator.DEBUG:
      print("Password: {TestPasswordValidator.VALID_PASS}")
      print("Hash (length {len(hashed)}): {hashed.hex()}")
      print("Salt (length {len(salt)}): {salt.hex()}")


  # Test to see if the same password that is hashed twice creates different hashes due to different salts
  def test_hash_salting_effectiveness(self):
    if TestPasswordValidator.DEBUG:
      print("\n--- Testing Hashing/Salting Effectiveness ---")
  
    hashed1, salt1 = self.validator.hash(TestPasswordValidator.VALID_PASS)
    hashed2, salt2 = self.validator.hash(TestPasswordValidator.VALID_PASS)
      
    # The salts must be different
    self.assertNotEqual(salt1, salt2, "Two randomly generated salts must be different.")
    
    # The resulting hashes must be different since the salts are different
    self.assertNotEqual(hashed1, hashed2, "Same password, different salts must create different hashes.")
      
    if TestPasswordValidator.DEBUG:
      print("Hash 1/Salt 1 generated.")
      print("Hash 2/Salt 2 generated.")
      print("Are the hashes equal? {hashed1 == hashed2} (Should be False)")


  # Test for successful password verification
  def test_verify_success(self):
    if TestPasswordValidator.DEBUG:
      print("\n Testing Verification (Success): ")

    hashed, salt = self.validator.hash(TestPasswordValidator.VALID_PASS)
    
    is_correct = self.validator.verify(TestPasswordValidator.VALID_PASS, hashed, salt)
    self.assertTrue(is_correct, "Verification should succeed when the password is correct.")

    if TestPasswordValidator.DEBUG:
      print("Verification of '{TestPasswordValidator.VALID_PASS}' is successful: {is_correct}")


  # Test for unsuccessful password verification
  def test_verify_failure(self):
    if TestPasswordValidator.DEBUG:
      print("\n Testing Verification (Failure): ")

    hashed, salt = self.validator.hash(TestPasswordValidator.VALID_PASS)
    incorrect_password = "NotTheCorrectPassword"
    
    is_incorrect = self.validator.verify(incorrect_password, hashed, salt)
    self.assertFalse(is_incorrect, "Verification should fail when the password is incorrect.")

    if TestPasswordValidator.DEBUG:
      print("Attempted verification with '{incorrect_password}' has failed: {not is_incorrect}")


  # Tests that running the hashing process with the same password and salt multiple times gives the same result every time
  def test_verify_with_known_salt(self):
    if TestPasswordValidator.DEBUG:
      print("\n Testing Verification with Known Salt Consistency: ")
  
    # Create a non-random salt
    known_salt = b'1' * 16 
    
    # Hash 1
    hashed1, salt_used = self.validator.hash(TestPasswordValidator.VALID_PASS, known_salt)
    
    # Hash 2
    hashed2, salt_used = self.validator.hash(TestPasswordValidator.VALID_PASS, known_salt)

    self.assertEqual(hashed1, hashed2, "Hashing the same password with same salt must create an identical hash.")
    
    # Verification using the known salt should still pass
    self.assertTrue(self.validator.verify(TestPasswordValidator.VALID_PASS, hashed1, known_salt), "Verification should succeed when using a pre-defined salt.")
    
    if TestPasswordValidator.DEBUG:
      print("Hash 1 and Hash 2 are identical: {hashed1 == hashed2}")
      print("Verification using identical hash/salt pair has been successful.")


# This allows running the tests directly from the command line
if __name__ == '__main__':
    unittest.main()
