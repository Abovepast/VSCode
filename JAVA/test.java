public class test {
    public static void main(String[] args) {   
        int[] countMax =  {2,4,6,3,3};
        printSeparate(countMax);
    }
    public static void printSeparate(int[] countMax) {
        for (int i = 0; i < countMax.length; i++) {
            System.out.print("+");
            for (int j = 0; j < countMax[i]+2; j++) {
                System.out.print("-");
            }
        }
        System.out.println("+");
    }
}