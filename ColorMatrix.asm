INCLUDE Irvine32.inc

.data
count DWORD ?

.code
main PROC

	mov eax, 0 + (0 * 16)
	mov ecx, 16
	L1:
		mov count, ecx
		push eax
		mov ecx, 16
		L2:
			call SetTextColor
			push eax
			mov al,'C'
			call WriteChar
			pop eax
			inc eax
		LOOP L2
		call crlf
		pop eax
		add eax, 16
		mov ecx, count
	LOOP L1

	call crlf
	call WaitMsg
	exit
main ENDP

END main