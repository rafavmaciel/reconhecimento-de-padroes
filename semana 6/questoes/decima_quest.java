public class decima_quest {
    
    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("./imagens/Cérebro.png");
        int numIntensidade = 256 -1 ;
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                img[i][j] = numIntensidade -img[i][j]  ;
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest10_4.png");

        
        
    }
}
