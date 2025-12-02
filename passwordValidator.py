# passwordValidator.py
# 
# Authors: Victoria Seusankar, ...
# 
# Date: 11/24/25


class passwordValidator:
  # Invariants
  # MIN_LENGTH: The minimum required length for a new password
  # MAX_LENGTH: The maximum allowed length for a new password
  # HASH_ALGORITHM: The cryptographic hash function used for hashing
  # ITERATIONS: The number of iterations 
  # SALT_SIZE: The size of the salts in bytes
  # HASH_KEY_LENGTH: The length of the derived key in bytes
  # DISALLOWED_CHARS_PATTERN: A pattern matching disallowed characters

  MIN_LENGTH: int = 8
  MAX_LENGTH: int = 16
  HASH_ALGORITHM: str = 'sha256'
  ITERATIONS: int = 200000 
  SALT_SIZE: int = 16
  HASH_KEY_LENGTH: int = 64
  DISALLOWED_CHARS_PATTERN: str = (“/”, “\”, “<”, “>”, “|”, “ “)

  # Constructor
  def __init__():
    pass

    
  # Checks to see if a password is valid
  # @param password: The password
  # @return: True if the password is valid, and false otherwise
  # @require: The password is a string
  # @ensure: returns true if all password requirements are met, and false otherwise
  def isValid(password: str):
    assert isinstance(password, str), "Password must be a string."
    
    # Validate the length
    if not (self.MIN_LENGTH <= len(password) <= self.MAX_LENGTH):
      return False

    # Check for Disallowed Characters
    for char in password:
      if char in DISALLOWED_CHARS_LIST:
        return False
            
    return True


  # Hashes a password
  def hash(password: str, salt: bytes = None):
    pass


  # Verifies a password
  def verify(password: str, stored_hash: bytes, salt: bytes):
    pass

