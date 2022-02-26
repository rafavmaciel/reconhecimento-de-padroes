public class quarta_quest {
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
        int[][] img = ImagemDigital.carregarImagem("./imagens/Fig0230(a)(dental_xray).png");
        int[][] img2 = ImagemDigital.carregarImagem("./imagens/Fig0230(b)(dental_xray_mask).png");
        double a = 0.5;
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                img[i][j] = (int)((int)(a *(img[i][j]))*((1-a)*img2[i][j]));
            }

        }
        corrigir(img);
        ImagemDigital.plotarImagem(img, "subtração");
        
    }
    
}
