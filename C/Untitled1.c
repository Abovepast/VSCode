#include <stdio.h>
#define MAX_NUM 40

struct student
{
    char ID[12];
    int MT,EN,PH,sum;
    float avg;
};


int main()
{
    int num;
    int sumc[3]={0,0,0};
    float avgc[3];
    struct student stu[MAX_NUM];

    printf("Input the total number of the students(n<40):\n ");
    scanf("%d", &num);

    if (num > MAX_NUM)
    {
        printf("Error: The number of students exceeds the maximum limit.\n");
        return 1;
    }

    printf("Input student' SID and score as: MT EN PH:\n ");
    for (int i = 0; i < num; i++)
    {
        scanf("%s", stu[i].ID);
        scanf("%d %d %d", &stu[i].MT, &stu[i].EN, &stu[i].PH);
        stu[i].sum = stu[i].MT + stu[i].EN + stu[i].PH;
        stu[i].avg = (float)stu[i].sum / 3;
        sumc[1]+=stu[i].MT;
        sumc[2]+=stu[i].EN;
        sumc[3]+=stu[i].PH;
    }
    for (int i=0;i<3;i++)
    {
        avgc[i]=(float)sumc[i]/3;
    }
    printf("Counting Result:\n");
    printf("Student's ID    MT    EN    PH    SUM    AVER\n");
    for (int i=0;i<num;i++)
    {
        printf("%12s    %d    %d    %d    %d    %f",stu[1].ID,stu[i].MT,stu[i].EN,stu[i].PH,stu[i].sum,stu[i].avg);
    }
    printf("SumofCourse     %d    %d    %d\n",sumc[1],sumc[2],sumc[3]);
    printf("AverofCourse    %f    %f    %f\n",avgc[1],avgc[2],avgc[3]);
    return 0;
}
