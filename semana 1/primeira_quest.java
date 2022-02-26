import java.util.ArrayList;
public class primeira_quest {
    public static void main(String[] args) {
        int[][] img = ImagemDigital.carregarImagem("Fig0207(a)(gray-level-band).png");
        ArrayList<Integer> shadesOfGray = new ArrayList<Integer>();
        // ImagemDigital.plotarImagem(img, "gradiente");
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                int value = img[i][j];
                if (shadesOfGray.contains(value) == false) {
                    shadesOfGray.add(value);
                }

            }

        }
        System.out.println(shadesOfGray.toString());

    }
}
