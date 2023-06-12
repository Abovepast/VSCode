//需要使用的元素
let items = document.querySelectorAll(".box_axis > div");
let move = document.querySelector(".move");

//初始化变量
let last=0;

//滑块和字体样式的变化

for(let i=0;i<Array.length;i++) {
	items[i].onmouseenter = function() {
		items[last].style.color = "black";
		this.style.color = "while";
		last = i;
		move.style.left = i*100 + 10 + "px";
	}
}