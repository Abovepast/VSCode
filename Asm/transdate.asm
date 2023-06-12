assume cs:codesg

codesg segment
    mov ax,0020h
    mov ds,ax   ;声明ds

    mov bx,0
    mov cx,40h
l1: mov [bx],bl
    inc bx
    loop l1

    mov ax,4c00h
    int 21h
codesg ends

end