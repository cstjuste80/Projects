

; Library Test #1: Integer I/O   (InputLoop.asm)
; Tests the Clrscr, Crlf, ReadInt, SetTextColor,
; WaitMsg, and WriteString procedures.
include Irvine32.inc
.data

 a SDWORD ?
 b SDWORD ?

BlueTextOnGray = blue + (lightGray * 16)
DefaultColor = lightGray + (black * 16)

prompt BYTE "Enter a integer: ",0
 result  BYTE "Result is: ",0
.code
main PROC
; Select blue text on a light gray background
    mov  eax,BlueTextOnGray
    call SetTextColor
    call Clrscr                     ; clear the screen
  
  mov dh,50
  mov dl,100
  
  call Gotoxy
    
    
 mov   edx,OFFSET prompt
    call  WriteString
    call  ReadInt                   ; input integer into EAX
    mov a,eax
  
    call Crlf
    call Crlf
                            ;
	
	
	

 call  WriteString
    call  ReadInt                   ; input integer into EAX
	add eax,a
	mov b,eax
	
	
	 call Crlf
	


mov edx,OFFSET result
  call WriteString
  call WriteInt

  call Crlf

  


; Return the console window to default colors
    call WaitMsg                    ; "Press any key..."
    mov  eax,DefaultColor
    call SetTextColor
    call Clrscr
    exit
main ENDP
END main
