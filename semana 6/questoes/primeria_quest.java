public class primeria_quest {
    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("./imagens/Fig0304(a)(breast_digital_Xray).png");
        int numIntensidade = 256 -1 ;
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                img[i][j] = numIntensidade -img[i][j]  ;
            }

        }
        ImagemDigital.salvarImagemPNG(img , "./plots/quest1.png");

        
        
    }
    
}
