; Cliff St.Juste
; Project 1
;DrawColorTexts
; 4/17/2018




include Irvine32.inc

.data
 YellowTextOnBlue = yellow + (blue * 16)
 COUNT = 4

 
Prompt BYTE "I'm the greatest in the world",0
 BlueTextOnGray = blue + (gray * 16)

 GreenTextOnBrown = green + (brown * 16)

 lightRedTextOnlightBlue = lightRed + (lightBlue * 16)
 
 
 colors DWORD YellowTextOnBlue,BlueTextOnGray,GreenTextOnBrown,lightRedTextOnlightBlue






.code
main PROC
 
 
mov  eax,yellow+(blue*16)
      call SetTextColor
  call Clrscr ; clearing the screen
 
 
mov ecx, COUNT
mov edi, OFFSET colors

 L1: 

 mov eax,[edi]
   call SetTextColor
   
   add edi,TYPE colors
 mov edx,OFFSET Prompt
  call WriteString
  
    call Crlf                       ; display a newline
	
	loop L1
	
	call waitMsg
  
  
  
  
  INVOKE ExitProcess,0
main ENDP
END main