public class segunda_quest {
    
    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("./imagens/Fig0308(a)(fractured_spine).png");
        double gama = 0.4;
        int l = 256 ;
        double c = Math.pow((l-1),(1-gama));
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                double pixel = (int)Math.pow(img[i][j],gama);
                img[i][j] =  (int)(c*pixel);
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest2_3.png");

        
        
    }
    
}
