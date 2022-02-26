public class quinta_quest {
    public static void main(String[] args) {
        int[][][] img = ImagemDigital.carregarImagemCor("./imagens/a4d88a27b6e6f33558a8e675b742-1458995.jpg");
        double gama = 1.5;
        int l = 256 ;
        double c = Math.pow((l-1),(1-gama));
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                for (int k = 0; j < img[1].length; j++) {
                    double pixel = (int)Math.pow(img[i][j][k],gama);
                    img[i][j][k] =  (int)(c*pixel);
            }
        }

        }
        ImagemDigital.salvarImagemCorPNG(img , "./plots/quest5_6.png");

}
}
