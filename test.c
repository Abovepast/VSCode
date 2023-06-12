// model:

// sets:
// item/1..10/:weight,value,x;
// endsets

// data:
// weight = 2 8 15 1 10 5 19 19 3 5;
// value = 20 1 7 14 19 9 18 5 2 8;
// enddata

// max = @sum(item(i):x(i)*value(i));

// @sum(item(i):x(i)*weight(i))<=50;
// @for(item(i):@bin(x(i)));

// end



// max z = 72*x1+54*x2
// s.t.    x1+x2<=50
//         12*x1+8*x2<=480
//         3*x1<=100
//         x1>=0,x2>=0



// model:

// max = 72*x1+64*x2;

// [milk] x1+x2<=50;
// [time] 12*x1+8*x2<=480;
// [cpct] 3*x1<100;

// end
