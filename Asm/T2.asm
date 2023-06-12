assume cs:code

code segment
    mov ax,cs
    mov ds,ax   ;将数据段地址指向代码段

    mov ax,0020h
    mov es,ax   ;es为复制的容器地址

    mov bx,0
    mov cx,17h    ;这个数字是不确定的，先设为2运行后知道代码长度再改
L1: mov al,[bx]
    mov es:[bx],al
    inc bx
    loop L1

    mov ax,4c00h
    int 21h
code ends
end