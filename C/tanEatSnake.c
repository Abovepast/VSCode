/*
̰����
BY��һҶ����\n���ɣ�C4droid
��Ϸʵ�֣�
�Ƚ����滭����������ʼ���ߺ�ʳ��
ÿ�����궼�����ͣ�������ʳ����塢��ǽ�廹�Ǳ���
�����������������ͷ�ķ���������β���ܸ�����ͷ�ķ����ƶ�
 ���ƶ��ǰ���ͷǰ��������ĳ���ͷ��ɾ����β������βǰ�������ĳ���β
*/
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#define MAXH 18
#define MAXW 18  //��bug���������һ����
#define UP '2'
#define DOWN '8'
#define LEFT '4'
#define RIGHT '6'
#define SNAKELEN 3 //�߳�ʼ����
#define N 3 //�Ѷ�
struct{
	char type;
	char*ch;
}
charwall = {
	1,"��"
},//ǽ��
charbg = {
	2,"��"
},//����
charfood = {
	3,"��"
},//ʳ��
charsnake = {
	4,"��"
};//����
struct xy{
	int x;
	int y;
}headxy,tailxy;//��¼��ͷ����β������
char atlasmap[MAXH][MAXW];//��ͼ���е�����
char direction[MAXH][MAXW];//��������βת�䷽��
int score;//����
int main(void);//����������������Ҫ����
void drawmap(void);//������ͼ
void createfood(void);//�����������ʳ��
void createsnake(void);//������
void loading(void);//α����
void init(void);//��ʼ��
void die(void);//����
void move(char key);//���ƶ�
char nextkey(char key,char inpkey);//�ж�����ķ����Ƿ����Ҫ��
void drawmap(void)//������ͼ
{
	int x,y;
	for(y = 0;y<MAXH;y++)
	{
		for(x = 0;x<MAXW;x++)
		{
			if(x==0||y==0||x==MAXW-1||y==MAXH-1)//��ΧһȦ��ǽ��
			{
				printf("%s",charwall.ch);
				atlasmap[y][x] = charwall.type;
			}
			else
				//��������
			{
				atlasmap[y][x] = charbg.type;
				printf("%s",charbg.ch);
			}
		}
		printf("\n");
	}
}
void createfood(void)//�����������ʳ��
{
	int x,y;
	srand(time(0));
	do
	{
		x = rand()%(MAXW-2)+1;
		y = rand()%(MAXH-2)+1;
	}while(atlasmap[x][y]!=charbg.type)
		;//����������ڲ��Ǳ���������������
	gotoxy(x+1,y+1);
	printf("%s",charfood.ch);
	atlasmap[x][y] = charfood.type;//����������Ϊʳ������
}
void createsnake(void)//������
{
	int x_centre,y_centre;
	int len;
	x_centre = MAXW/2+SNAKELEN/2;
	y_centre = MAXH/2;
	for(len = 1;len<=SNAKELEN;len++)
	{
		gotoxy(x_centre-len+1,y_centre+1);
		printf("%s",charsnake.ch);
		//�ж���ͷ����β
		if(len==1)//��ͷ����
		{
			headxy.x = x_centre;
			headxy.y = y_centre+1;
		}
		else if(len==SNAKELEN)//��β����
		{
			tailxy.x = x_centre-len+1;
			tailxy.y = y_centre+1;
		}
		atlasmap[x_centre-len][y_centre] = charsnake.type;//�������͸ĳ�����
		direction[x_centre-len][y_centre] = RIGHT;//��ʼ��������ΪRIGHT
	}
}

void init(void)
{
//	loading();//α����
	drawmap();//���Ƶ�ͼ
	createsnake();//��ʼ��̰����
	createfood();//����ʳ��
	gotoxy(0,MAXH+3);
	printf("������%d\n",score = 0);
	puts("BY��һҶ����\n���ɣ�C4droid");
	gotoxy(0,MAXH+1);//�������ƶ���ͼ���������
}
void die(void)
{
	sleep(1);
	clrscr();
	printf("��Ϸ�������÷֣�%d\n���������\n",score);
	getch();
	clrscr();
	main();//Ӧ�ò��Ǻܺ�����������ô�ֱ��Ľ���ɣ�
}
void move(char key)//���ƶ�
{
	extern struct xy headxy,tailxy;//�ٴ�����
	direction[headxy.x-1][headxy.y-1] = key;//�Ƚ���ͷҪȥ�ķ�����ڸ������ڣ���β����������ж�ȥ��
	switch(key)
	{
	case RIGHT:
		++headxy.x;
		break;
	case UP:
		--headxy.y;
		break;
	case LEFT:
		--headxy.x;
		break;
	case DOWN:
		++headxy.y;
		break;
	}
	if(atlasmap[headxy.x-1][headxy.y-1]==charwall.type
			||atlasmap[headxy.x-1][headxy.y-1]==charsnake.type)//�ж��Ƿ�ײǽ��ҧ�Լ�
	{
		die();
	}
	gotoxy(headxy.x,headxy.y);
	printf("%s",charsnake.ch);
	//�ж��Ƿ�Ե�ʳ�����Ե�����β���������Ѹ����������ת��������
	if(atlasmap[headxy.x-1][headxy.y-1]==charfood.type)
	{
		createfood();
		score++;//������1
		gotoxy(0,MAXH+3);
		printf("������%d",score);
		atlasmap[headxy.x-1][headxy.y-1] = charsnake.type;
	}
	else
		//���û�Ե�����β���ϣ��������goto���
	{
		atlasmap[headxy.x-1][headxy.y-1] = charsnake.type;//��ͷǰ��
		gotoxy(tailxy.x,tailxy.y);//���굽��β
		atlasmap[tailxy.x-1][tailxy.y-1] = charbg.type;//����β�ĳɱ�������������ǰ����
		printf("%s",charbg.ch);
		switch(direction[tailxy.x-1][tailxy.y-1])//�ж���ͷ���������ʱ�������û��
		{
		case RIGHT:
			direction[tailxy.x-1][tailxy.y-1] = 0;//���������ڵķ������
			++tailxy.x;//������Ӧ�ķ���
			break;
		case UP:
			direction[tailxy.x-1][tailxy.y-1] = 0;
			--tailxy.y;
			break;
		case LEFT:
			direction[tailxy.x-1][tailxy.y-1] = 0;
			--tailxy.x;
			break;
		case DOWN:
			direction[tailxy.x-1][tailxy.y-1] = 0;
			++tailxy.y;
			break;
		}
	}
	gotoxy(0,MAXH+1);//����ͼ����з�������
}
char nextkey(char key,char inpkey)//�ж�����ķ����Ƿ����Ҫ��
{
	char next;
	if(inpkey==' ')//����ǿո�����ͣ��Ϸ
	{
		inpkey = getch();
	}
	//�ж��û��ķ����Ƿ��෴������෴������Ƿ�������ϴκϷ�����
	if((inpkey==UP&&key!=DOWN)||(inpkey==DOWN&&key!=UP)
			||(inpkey==LEFT&&key!=RIGHT)||(inpkey==RIGHT&&key!=LEFT))
		next = inpkey;
	else
		next = key;
	return next;
}
int main(void)
{
	init();//��ʼ����Ϸ
	char key = RIGHT,inpkey;//���巽��Ĭ������
	while(1)//����ѭ��������
	{
		if(kbhit())//�ж����������Ƿ�������
		{
			inpkey = getch();//���������е����ݱ�������
			key = nextkey(key,inpkey);//���غϷ�����
		}
		move(key);//���ƶ�
		putchar('\n');//�������ݣ����������
		usleep(1000000/N);//�ƶ��ٶ�
	}
	return 0;
}