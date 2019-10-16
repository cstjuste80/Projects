

include Irvine32.inc

.data
 YellowTextOnBlue = yellow + (blue * 16)
 Count = 4

 
Prompt BYTE "I'm the greatest in the world",0
 BlueTextOnGray = blue + (gray * 16)

 GreenTextOnBrown = green + (brown * 16)

 lightRedTextOnlightBlue = lightRed + (lightBlue * 16)
 
 
 colors BYTE YellowTextOnBlue,BlueTextOnGray,GreenTextOnBrown






.code
main PROC
 
 
mov  eax,yellow+(blue*16)
      call SetTextColor
  call Clrscr ; clearing the screen
 
  
 L1: mov eax,OFFSET prompt
  call WriteString
   call ReadInt                    ; input integer into EAX
    call Crlf                       ; display a newline


  
  
  
  
  INVOKE ExitProcess,0
main ENDP
END main