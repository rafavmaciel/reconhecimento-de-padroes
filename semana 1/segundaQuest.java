public class segundaQuest {
    public static void main(String[] args) {
       int[][] img = new int[300][300];
       int corQuadradoExt = 192;
        // ImagemDigital.plotarImagem(img, "gradiente");
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {

                if(i>=100 && i<=200){

                    if(j>=100 && j<=200){
                        img[i][j] = 128;
                        
                    }
                    else{
                        img[i][j] = corQuadradoExt;
                    }

                }
                else{
                    img[i][j] = corQuadradoExt;
                }
               
            }

        }
        ImagemDigital.plotarImagem(img,"quadrado");
    }
    
}
