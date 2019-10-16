; AddTwo.asm - adds two 32-bit integers.
; Chapter 3 example
INCLUDE Irvine32.inc
.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

; adding a variable from page 54
.data ; thid id the data area

buffer BYTE 21 DUP(0)
byteCount DWORD ?
prompt BYTE "Enter something:",0
lc DWORD ?
.code
main proc

mov ecx,10
ECHOALOT:
mov edx,OFFSET prompt
call WriteString

mov edx,OFFSET buffer
save loop count
mov lc,ecx
mov ecx,SIZEOF buffer
call ReadString
mov byteCount,eax

call WriteString
call Crlf

mov ecx,lc


LOOP echoalot
call ReadString




	invoke ExitProcess,0
main endp
end main