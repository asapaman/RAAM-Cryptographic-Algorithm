# RAAM-Cryptographic-Algorithm-Working-Method

 RAAM(Rahul-Akancha-Aman-Meraj): We proposed a new algorithm to tackle the Key search and brute force attack named RAAM(Rahul-Akancha-Aman-Meraj) Algorithm.  This is a Symmetric-key stream cipher designed by us. DES is an implementation of a Feistel Cipher which uses a 16 round Feistel structure while this algorithm uses 10 rounds which reduces the time complexity. It is having a variable key having a minimum length of 4. It is developed to mitigate the brute force attack which was very much possible on other present ciphers.



The algorithm design breaks down into the following steps: 

Encryption 
P = Plain Text
K = Key (Length should be more than 4)
1. Generate the SHA256 hash of Key.
2. Append half of the hash value before and half of the value after P. 
3. Check the length of new plain text is divisible by the length of the key or not, if it completely divisible jump to step 5 else continue.
4. If the length of new plain text is not divisible by key length then find the remainder and subtract it from the length of the key.
-> If the difference is greater than 2 then subtract that this and append the same number of    "Z" and will write the number in the last two digit
	-> If the difference is 2 or 1 then append the respective no of Z.
5. Now the length of plain text is completely divisible by key length, then find quotient Q.
 6. Now form K*Q matrix and fill it with the plain text row-wise.
7. implement encryption by adding matrix char from left to right with key respectively.
8. Once step seven is completed on each row read column-wise starting from column 1, row 1.
9. Pass the values to step 6 and perform it 10 times
10. Once it performs 10 times the output will be the encrypted text.
Decryption
E -> Encrypted txt
K -> Key
1. Find Quotient Q = Len(E)/Len(K)
2. Form matrix of Lk*Q and fill it with encrypted text column-wise.
3. Perform decryption from left to right on each row
	-> Perform step 2 and step 3 ten times.
4. After decrypting 10 times remove the padding which was added before and after the text(SHA256).
5. Remove the appended "Z" or if there is a digit then count the digit and remove that number of "Z" from the text.
6. After removing everything we will get our original plain text.






