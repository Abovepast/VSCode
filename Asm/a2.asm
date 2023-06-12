assume cs:code
code segment
start:
    mov al,0dh
    call Liuweipei
    mov ah,4ch
    int 21h
Liuweipei proc
    cmp al,10
    jc,k1
    add al,7
k1:
    add al,30h
    mov dl,al
    mov ah,2
    int 21h
    ret
code ends
end start

