Private Sub Command1_Click()
    Dim arr(9) As Integer
    Dim i As Integer
    
    '从键盘输入10个整数
    For i = 0 To 9
        arr(i) = InputBox("请输入第" & (i + 1) & "个整数")
    Next
    
    '调用求最大值函数
    Dim max As Integer
    max = GetMax(arr)
    MsgBox "最大值为：" & max
    
    '调用求平均值函数
    Dim avg As Double
    avg = GetAvg(arr)
    MsgBox "平均值为：" & avg
    
    '调用排序函数
    Sort(arr)
    
    '将排序后的数组输出到窗体上
    Dim str As String
    For i = 0 To 9
        str = str & arr(i) & " "
    Next
    MsgBox "排序后的数组为：" & str
End Sub

'求最大值函数
Function GetMax(arr() As Integer) As Integer
    Dim max As Integer
    max = arr(0)
    Dim i As Integer
    For i = 1 To UBound(arr)
        If arr(i) > max Then
            max = arr(i)
        End If
    Next
    GetMax = max
End Function

'求平均值函数
Function GetAvg(arr() As Integer) As Double
    Dim sum As Integer
    Dim i As Integer
    For i = 0 To UBound(arr)
        sum = sum + arr(i)
    Next
    GetAvg = sum / (UBound(arr) + 1)
End Function

'排序函数（冒泡排序）
Sub Sort(arr() As Integer)
    Dim i As Integer, j As Integer
    For i = 0 To UBound(arr) - 1
        For j = i + 1 To UBound(arr)
            If arr(j) < arr(i) Then
                '交换两个数的位置
                Dim temp As Integer
                temp = arr(j)
                arr(j) = arr(i)
                arr(i) = temp
            End If
        Next
    Next
End Sub