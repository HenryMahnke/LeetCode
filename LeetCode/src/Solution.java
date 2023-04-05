class Solution {
    int value = 0;
    char[] temp;
    int future;
    int current;
    public static void main(String[] Args){

    }
    
    public int romanToInt(String s) {
        for(int i = 0; i< s.length(); i++){
            current = getValue(s.charAt(i));
            if((s.charAt(i+1)) != (Character)null){
             future = getValue(s.charAt(i+1));
            }
            if(future>current){
                value += future-current;
                i++;
                    
            }
            else{
                value += current;
            }
            }
                        return value;

            }

    public int getValue(char c){
        int temp = 0;
        switch(c){
            case 'I':
                temp =1;
                break;
            case 'V':
                temp = 5;
                break;
            case 'X':
                temp =10;
                break;
            case 'L':
                temp = 50;
                break;
            case 'C':
                temp = 100;
                break;
            case 'D':
                temp = 500;
                break;
            case 'M':
                temp = 1000;
                break;
            default:
                temp =0;
                break;
        }
        return temp;
    }
    }