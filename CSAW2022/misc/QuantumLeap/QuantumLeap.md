# Quantum Leap

### Description

My friend took the quantum leap and purchased a quantum computer with two qubits. They mentioned using a quantum logic gate to input the flag and they gave me the computers output. I have been stuck and Can NOT figure out the flag.
 
## Solution
 
We are given a file containing
```
wxqvn$Zae${deyZv$d"i
```
that is the flag after passing through a quantum logic gate. We started by searching some information on quantum gate. The description told us that we were looking for gates with 2 qubit as inputs. Helped by the uppercase NOT in the description of the challenge it was clear that we needed to apply the CNOT gate (this is because the reverse of the CNOT gate is the CNOT gate itself). We immediately tought of converting the string to binary. Using cyberchef we got
```
011101110111100001110001011101100110111000100100010110100110000101100101001001000111101101100100011001010111100101011010011101100010010001100100001000100110100100001010
```
After a few attempts we understood that each digit represents a qubit and the gate acts on each pair of qbits (if the first is 1 it reverses the second, otherwise it does not do anything). We wrote a quick script and got the following:
```
011001100110110001100001011001110111101100110100010111110111000101110101001101000110111001110100011101010110110101011111011001110011010001110100001100110111110100001111
```
that is going back to ASCII
```
flag{4_qu4ntum_g4t3}
```
