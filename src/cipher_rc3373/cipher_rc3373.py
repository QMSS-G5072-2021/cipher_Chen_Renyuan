
def cipher(text, shift, encrypt=True):
    """
    In Caesar cipher, each letter is replaced by a letter some fixed number of positions down the alphabet.
    This function helps people to encrypt and decrypt the code with Caesar cipher.

    Parameters
    ----------
    text : A string value to be enciphered or deciphered.
    shift :  An int value that determines the number of shift.
    encrypt: equals 'True' when encrypting and 'False' when decrypting.
    
    Returns
    -------
    A new string value that is enciphered or deciphered based on the inputs.

    Examples
    --------
    >>> from cipher_rc3373 import cipher_rc3373
    >>> cipher_rc3373.cipher('Love', 1, encrypt=True)
    'Mpwf'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
