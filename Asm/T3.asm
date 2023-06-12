assume cs:code,ds:data,ss:stack

data segment    ;定义一些数据，地址由系统分配
    dw 0123h,0456h,0789h,0abch,0defh,0fedh,0cbah,0987h
data ends

stack segment   ;定义一个栈，地址由系统分配
    dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stack ends

code segment
start:  ;用来运行的代码由此开始
    mov ax,stack
    mov ss,ax   ;将stack与ss堆栈段寄存器绑定
    mov sp,32   ;16个字，32字节

    mov ax,data
    mov ds,ax   ;将data与ds数据段寄存器绑定

    push ds:[0]
    push ds:[2]
    pop ds:[2]
    pop ds:[0]

    mov ax,4c00h
    int 21h
code ends
end start