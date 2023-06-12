assume cs:code

a segment
    dw 1,2,3,4,5,6,7,8,9,0ah,0bh,12,13,14,0fh,0ffh
a ends

b segment
    dw 0,0,0,0,0,0,0,0
b ends

code segment
start:
    mov ax,b
    mov ss,ax
    mov sp,16

    mov ax,a
    mov ds,ax

    mov bx,0
    mov cx,8
L1: push ds:[bx]
    add bx,2
    loop L1

    mov ax,4c00h
    int 21h

code ends
end start