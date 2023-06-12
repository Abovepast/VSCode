assume cs:code

a segment
    db 1,2,3,4,5,6,7,8
a ends

b segment
    db 1,2,3,4,5,6,7,8
b ends

c segment
    db 0,0,0,0,0,0,0,0
c ends

code segment
start:
    mov ax,a
    mov ds,ax
    
    mov cx,8
    mov bx,0
L1: mov ax,ds:[bx]
    add bx,20h  ;注意不能用"mov bx,20h",因为bx会变
    mov ds:[bx],ax  ;依次将a段的数据放进20h开始的段中
    ;mov ds:[bx+20h],ax 以上两句可以简化为这样

    sub bx,10h
    mov ax,ds:[bx]
    add bx,10h
    add ax,ds:[bx]
    mov ds:[bx],ax
    
    sub bx,20h  ;恢复现场
    
    inc bx
    loop L1

code ends
end start