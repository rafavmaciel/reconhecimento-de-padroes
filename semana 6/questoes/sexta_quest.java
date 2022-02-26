public class sexta_quest {

    static void carregarA(int[][] img) {
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                if (img[i][j] < 64){
                    img[i][j] = (int)(0.5*img[i][j]);
                }
                if (img[i][j] >= 64 && img[i][j] <= 192){
                    img[i][j] = (int)((1.5*img[i][j])-65);
                } 
                else{
                    img[i][j] = (int)((0.5*img[i][j])+128);
                }
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest6_A.png");

    }
    static void carregarB(int[][] img) {
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                if (img[i][j] < 107){
                    img[i][j] = 0;
                }
                else{
                    img[i][j] = 255;
                }
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest6_B.png");

    }

    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("./imagens/Fig0310(b)(washed_out_pollen_image).png");
        int[][] img2 = ImagemDigital.carregarImagem("./imagens/Fig0310(b)(washed_out_pollen_image).png");
        carregarA(img);
        carregarB(img2);
        
    }
    
}
