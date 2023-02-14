### README ###

My little rudimentary tool for monoalphabetic substitution ciphers. The encryption part was originally written in C as part of the CS50x course. Then I wrote the the decryption part for fun to see if I could do it.
After I made it work I transferred the whole thing to Python just to see how much shorter the code would be than it was in C. :D
Finally I added a (admittedly very crude) GUI with tkinter.

###

MANUAL

Input the message you want to encrypt or decrypt into the field on the left.

The field in the center is where your encryption key goes. This is a monoalphabetic substitution tool, so the key has to be a complete alphabet (all 26 letters with no duplicates, jumbled in any way you want) for this to work properly. 
It will then replace the letters of our actual alphabet with the letters you've put into their respective places. Let's say you're using the key ZYXWVUTSRQPONMLKJIHGFEDCBA. The tool will then replace all the As in your text with Zs, 
the Bs with Ys, the Cs with Xs and so on.

You can use the copy button on the bottom right to copy the output text to your clipboard.


For what it's worth, enjoy :D


Made by Daniel Reitz, 2022