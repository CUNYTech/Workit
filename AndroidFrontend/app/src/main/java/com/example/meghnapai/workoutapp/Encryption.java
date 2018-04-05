package com.example.meghnapai.workoutapp;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;

public class Encryption
{
    private byte[] key;

    private static final String ALGORITHM = "AES";	// Uses ECB as a default. May need to change it due to security issues.

    public Encryption(byte[] key)
    {
        this.key = key;
    }

    /**
     * Encrypts the given plain text
     *
     * @param plainText The plain text to encrypt
     */
    public byte[] encrypt(byte[] plainText) throws Exception
    {
        SecretKeySpec secretKey = new SecretKeySpec(key, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        return cipher.doFinal(plainText);
    }

    public byte[] getKey() {
        return key;
    }

    /**
     * Decrypts the given byte array
     *
     * @param cipherText The data to decrypt
     */
    public byte[] decrypt(byte[] cipherText) throws Exception
    {
        SecretKeySpec secretKey = new SecretKeySpec(key, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, secretKey);

        return cipher.doFinal(cipherText);
    }

    public static void main(String[] args) throws Exception
    {
        byte[] encryptionKey = "MZygpewJsCpRrfOr".getBytes(StandardCharsets.UTF_8);     // placeholder stuff
        byte[] plainText = "Hello world!".getBytes(StandardCharsets.UTF_8);             // placeholder stuff
        Encryption newEncrypt = new Encryption(
                encryptionKey);
        byte[] cipherText = newEncrypt.encrypt(plainText);
        byte[] decryptedCipherText = newEncrypt.decrypt(cipherText);

        System.out.println(new String(plainText));
        System.out.println(new String(cipherText));
        System.out.println(new String(decryptedCipherText));
    }
}