assume cs:code,ds:data
data segment
    buf db 34h,?,?
data ends 

code segment
start:
    mov ax,data
    mov ds,ax

    mov al,buf

    shr al,cl
    mov buf+1,al
    mov al,buf
    and al,0fh
    mov buf+2,al
    mov ah,4ch
    int 21h
code ends
end start