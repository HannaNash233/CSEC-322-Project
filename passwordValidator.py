# passwordValidator.py
# 
# Authors: Victoria Seusankar
# 
# Date: 11/24/25

import hashlib
import os

class passwordValidator:
  # Invariants
  # MIN_LENGTH: The minimum required length for a new password
  # MAX_LENGTH: The maximum allowed length for a new password
  # HASH_ALGORITHM: The cryptographic hash function used for hashing
  # ITERATIONS: The number of iterations 
  # SALT_SIZE: The size of the salts in bytes
  # HASH_KEY_LENGTH: The length of the derived key in bytes
  # DISALLOWED_CHARS: A pattern matching disallowed characters

  MIN_LENGTH: int = 8
  MAX_LENGTH: int = 16
  HASH_ALGORITHM: str = 'sha256'
  ITERATIONS: int = 200000 
  SALT_SIZE: int = 16
  HASH_KEY_LENGTH: int = 64
  DISALLOWED_CHARS: str = (“/”, “\”, “<”, “>”, “|”, “ “)

  # Constructor
  # @require: None
  # @ensure: The validator object is initialized with constants
  def __init__():
    # This class is used as a container for static constants and methods, so there is no additional information needed.
    pass

    
  # Checks to see if a password is valid
  # @param password: The password
  # @return: True if the password is valid, and false otherwise
  # @require: The password is a string
  # @ensure: Returns true if all password requirements are met, and false otherwise
  def isValid(password: str):
    assert isinstance(password, str), "Password must be a string."
    
    # Validate the length
    if not (self.MIN_LENGTH <= len(password) <= self.MAX_LENGTH):
      return False

    # Check for Disallowed Characters
    for char in password:
      if char in DISALLOWED_CHARS:
        return False
            
    return True


  # Hashes a password
  # @param password: The password
  # @param salt: A salt byte string; if salt = None, a new salt is generated
  # @return: A tuple containing the password and salt as bytes
  # @require: The password is a string and the salt is either None or bytes
  # @ensure: Returns a salted hash from the password
  def hash(password: str, salt: bytes = None):
    assert isinstance(password, str), "Password must be a string."
    assert salt is None or isinstance(salt, bytes), "Salt must be bytes or None."
        
    if salt is None:
      # Generate a new, cryptographically secure random salt
      salt = os.urandom(self.SALT_SIZE)
      
    # Hash the password using PBKDF2_HMAC
    password_hash = hashlib.pbkdf2_hmac(self.HASH_ALGORITHM, password.encode('utf-8'), salt, self.ITERATIONS, dklen = self.HASH_KEY_LENGTH)
    
    # Return the hash and salt
    return password_hash, salt


  # Verifies a password
  # @param password: The password 
  # @param stored_hash: The generated and stored hash
  # @param salt: The salt used to generate the stored_hash
  # @return: True if the password matches the stored hash, and false otherwise 
  # @require: The password is a string and the stored_hash and salt are valid byte sequences
  # @ensure: Returns true if the re-hashed password matches the stored_hash.
  def verify(password: str, stored_hash: bytes, salt: bytes):
    assert isinstance(password, str), "Password must be a string."
    assert isinstance(stored_hash, bytes), "Stored hash must be bytes."
    assert isinstance(salt, bytes), "Salt must be bytes."
        
    # Re-hash the cleartext password using the stored salt
    attempted_hash = hashlib.pbkdf2_hmac(self.HASH_ALGORITHM, password.encode('utf-8'), salt, self.ITERATIONS, dklen = self.HASH_KEY_LENGTH)
    
    # Compare the hashes to avoid leaking information about the password length.
    return attempted_hash == stored_hash

