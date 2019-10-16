




include Irvine32.inc

.data

rows = 30
columns = 120

 a SDWORD ?
 b SDWORD ?


GrayTextOnBlue = Gray + (Blue * 16)
RedTextOnRed = Red + (Red * 16 )

DefaultColor = lightGray + (Red * 16)



prompt BYTE "Blue Screen of Death!! ",0
 
.code
main PROC
; Select blue text on a light gray background
    mov  eax,GrayTextOnBlue
    call SetTextColor
    call Clrscr                     ; clear the screen
  
  
  
  ;Creating the border red
    mov eax,RedTextOnRed
    call SetTextColor
    
	mov al, ' '
	

    
 mov dh, 0
 mov dl, 0
 
 call gotoxy

  

 mov ecx, columns 




 L1:
  
   
  call WriteChar
 
  loop L1
  


  mov dh, rows -1
 mov dl, 0
 
 call gotoxy

  

 mov ecx, columns 




 L2:
  
   
  call WriteChar
 
  loop L2
  
  

 mov ecx, rows 

  mov dh, 0
 mov dl, columns -1
 
 call gotoxy

 L3: 

 call WriteChar

 inc dh
 
 call gotoxy

 loop L3
 
 mov dh, 0
 mov dl, 0
 
 call gotoxy
 
 mov ecx, rows

 L4:

  call WriteChar
  
  inc dh

  call gotoxy
  

  loop L4



  mov dh,15
  mov dl,48
  
  call Gotoxy

  ; Changing color back

    mov  eax,GrayTextOnBlue
    call SetTextColor
     
    
 mov   edx,OFFSET prompt
    call  WriteString
   
   



   mov dh, rows-2
   mov dl, 2
   call	gotoxy


; Return the console window to default colors
    call WaitMsg                    ; "Press any key..."
    mov  eax,DefaultColor
    call SetTextColor
    call Clrscr
    exit
main ENDP
END main