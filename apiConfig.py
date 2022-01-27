import pickle
from keras.models import load_model
from attention import attention

# Hello Problem
# "public class HelloWorld {\n    public static void main(String[] args) {\n    }\n    System.out.println(\"Hello\"); {\n}"

# For Problem
# "public class sample {\n    public static void main(String[] args) {\n        for (int i = 0; i < 5; i++) {\n            System.out.println(i); {\n        }\n    }\n}"

# EVEN ODD PROBLEM
# "import java.util.Scanner;\n\npublic class Main{\n   public static void main(String []args){\n     Scanner input = new Scanner(System.in); {\n     int num = input.nextInt();\n\n     if ( num % 2 == 0 )\n        System.out.println(\"even\");\n     else\n        System.out.println(\"odd\");\n   }\n}"

# with open('pickleFiles/old_javaKeywords.pickle', 'rb') as f:
# with open('pickleFiles/javaKeywords.pickle', 'rb') as f:  # max_length-350
with open('pickleFiles/12-15-javaKeywords.pickle', 'rb') as f:  # max_length-250
    javaKeywords = pickle.load(f)

# with open('pickleFiles/old_ixtow.pickle', 'rb') as f:
# with open('pickleFiles/ixtow.pickle', 'rb') as f:  # max_length-350
with open('pickleFiles/12-15-ixtow.pickle', 'rb') as f:  # max_length-250
    ixtow = pickle.load(f)

# max_length = 494
# model = load_model("models/insertion_sort.h5",

# max_length = 250
# model = load_model("models/1-24-bilstm.h5",

max_length = 250
model = load_model("models/1-24-bilstm.h5",
                   custom_objects={'attention': attention()})
