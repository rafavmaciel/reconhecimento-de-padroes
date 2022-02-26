public class terceira_quest {
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
        int[][] img = ImagemDigital.carregarImagem("./imagens/Fig0308(a)(fractured_spine).png");
        double log = 0.6;
        int l = 256 ;
        double c = (l-1)/Math.log(l);
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                int s = (int) (c * Math.log(1+img[i][j]));
                img[i][j] = (int) ((Math.log(s)) / (Math.log(log)) );
            }

        }
        //corrigir(img);
       
        ImagemDigital.salvarImagemPNG(img , "./plots/quest3.png");

        
        
    }
}
