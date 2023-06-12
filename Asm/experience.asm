;1

MOV AX, A
ADD AX, B
ADD AX, C
JZ ZERO  ; 若AX等于0则跳转到ZERO处
MOV D, AX
JMP END   ; 跳转到END处

ZERO:
MOV A, 0
MOV B, 0
MOV C, 0
MOV D, 0

END

;2
.MODEL SMALL
.STACK 100H
.DATA
    LEDtable DB 0c0h,0f9h,0a4h,0b0h,99h,92h,82h,0f8h
             DB 80h,90h,88h,83h,0c6h,0c1h,86h,8eh

.CODE
.STARTUP
    MOV AH, 2 ; 设置打印字符函数号
    MOV DL, '7' ; 待转换的数字
    SUB DL, '0' ; 将ASCII码转换成数值
    MOV BL, DL ; 将待转换数字保存到BL中
    AND BL, 0FH ; 保留低四位
    SHL BL, 1 ; 将BL左移一位，相当于乘以2
    MOV AL, LEDtable[BL] ; 根据转换表获取LED显示代码的高字节
    MOV AH, LEDtable[BL+1] ; 获取LED显示代码的低字节
    INT 21H ; 在屏幕上输出字符
.EXIT
END

;3
.MODEL SMALL
.STACK 100H
.DATA
    bufX DB 10 ; 变量bufX
    bufY DB 15 ; 变量bufY
    bufZ DB ? ; 变量bufZ
.CODE
.STARTUP
    MOV AL, bufX ; 将bufX中的值移动到AL寄存器中
    CMP AL, bufY ; 比较AL和bufY中的值
    JAE GREATER_OR_EQUAL ; 如果AL大于等于bufY，则跳转到GREATER_OR_EQUAL处
    MOV bufZ, bufY ; 否则将bufY中的值移动到bufZ中
    JMP END_PROGRAM ; 跳转到程序结束处

GREATER_OR_EQUAL:
    MOV bufZ, bufX ; 将bufX中的值移动到bufZ中

END_PROGRAM:
    ; 程序结束
.END

;4
.MODEL SMALL
.STACK 100H
.DATA
    bufX DW -1234 ; 变量bufX，注意为16位有符号数
    signX DB ? ; 符号状态，0表示正数，FFh表示负数
.CODE
.STARTUP
    MOV AX, bufX ; 将bufX的值移动到AX寄存器中
    SAR AX, 15 ; 对AX右移15位，即保留最高位（符号位），并将其复制到其他位上
    MOV signX, AH ; 将移位后的AH值（即符号位）保存到signX中

END_PROGRAM:
    ; 程序结束
.END