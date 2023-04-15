.model small
.stack 100h
.data
    msg db 'Enter a capital letter:$'
    input db ?
    output db ?
.code
main proc
    mov ax,@data
    mov ds,ax
    lea dx,msg
    mov ah,9
    int 21h ; print message
    mov ah,1
    int 21h ; read input character
    mov bl,al ; save input character
    cmp al,'A'
    jb exit ; if input character is less than 'A', exit program
    cmp al,'Z'
    ja exit ; if input character is greater than 'Z', exit program
    add al,32 ; convert capital letter to small letter
    mov output,al ; save output character
    lea dx,output
    mov ah,9
    int 21h ; print output character
exit:
    mov ah,4ch ; return control to DOS
    int 21h 
main endp 
end main 