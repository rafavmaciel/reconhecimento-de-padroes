public class setima_quest {
    static void carregarA(int[][] img) {
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                if (img[i][j] >= 64 && img[i][j] <= 192){
                    img[i][j] = 153;
                } 
                else{
                    img[i][j] = 25;
                }
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest7_A.png");

    }
    static void carregarB(int[][] img) {
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                if (img[i][j] >= 64 && img[i][j] <= 192){
                    img[i][j] = 204;
                } 
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest7_B.png");

    }

    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("./imagens/Fig0312(a)(kidney).png");
        int[][] img2 = ImagemDigital.carregarImagem("./imagens/Fig0312(a)(kidney).png");
        carregarA(img);
        carregarB(img2);
        
    }
    
}

    
