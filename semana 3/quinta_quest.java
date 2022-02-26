public class quinta_quest {

    static void corrigir(int[][] img) {
        //pega maximo e minimo da img
        int max = 0;
        int min = 255;
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                max = Math.max(max, img[i][j]);
                min = Math.min(min, img[i][j]);
            }
        }

        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                img[i][j] = (255 * (img[i][j]-min))/ (max-min);
            }

        }
    }

    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("./ruido/lena1.png");
        
        for (int k = 2; k < 11; k++) {
            int[][] img2 = ImagemDigital.carregarImagem("./ruido/lena"+k+".png");
            for (int i = 0; i < img.length; i++) {
                for (int j = 0; j < img[0].length; j++) {
                    img[i][j] = img[i][j]+img2[i][j];
                }
    
            }
        }
        corrigir(img);
        ImagemDigital.plotarImagem(img, "soma");

        
        
    }
    
    
}
