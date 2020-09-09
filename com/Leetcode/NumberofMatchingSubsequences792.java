package com.Leetcode;

public class NumberofMatchingSubsequences792 {

    public static int isSubsequence(char[] s,char[] word) {
        int i = 0, j = 0;
        if (s.length < word.length) 
            return 0;
        while(j < word.length && i < s.length) {
            if (s[i] == word[j]) {
                i++;
                j++;
            } else {
                i++;
            }
        }     
        return (j == word.length) ? 1 : 0;
    }

    public static int numMatchingSubseq(String S, String[] words) {
        int total = 0;
        char[] string = S.toCharArray();
        for (String word : words) {
            total += isSubsequence(string, word.toCharArray());
        }
        return total;
    }

    public static void main(String[] args) {
        System.out.println(numMatchingSubseq(
                "ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugpeekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrsurrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvndigovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryzdmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzkhndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjyljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnhrptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxjhsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd",
                new String[] { "iowuuudrgzmw", "azfcxtvhkruvuturdicnucvndigovkzrq", "ylmmo", "maptilrbfpjxiarmwalhbd",
                        "oqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqgl", "ytldcdlxqbaszbuxsacqwqnhrewhagldzhr",
                        "zeeab", "cqie", "pvrazfcxtvhkruvuturdicnucvndigovkzrqiya",
                        "zxnvpluwicurrtshyvevkriudayyysepzq", "wyhxltligahroyshfn", "nhrewhagldzhryzdmmrwn",
                        "yqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmw", "nhrptuugyfsghluythksqhmxlmggtcbdd",
                        "yligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjsc",
                        "zdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzq", "ncygycdpehteiugqbptyqbvokpwovbnplshnzafun",
                        "gdzutwgjofowhryrubnxkahocqjzww", "eppapjoliqlhbrbgh", "qwhgobwyhxltligahroys",
                        "dzutwgjofowhryrubnxkah", "rydhxkdhffyytldcdlxqbaszbuxs",
                        "tyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjc", "khvyjyrydhxkdhffyytldcdlxqbasz",
                        "jajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqn", "ppapjoliqlhbrbghq",
                        "zmwwxzjckmaptilrbfpjxiarm", "nxkahocqjzwwagqidjhwbunvlchoj",
                        "ybfxpvqywqjdlyznmojdhbeomyjqptltp", "udrgzmwnxae", "nqglnpjvwddvdlmjjyzmww",
                        "swlvtlbmkrsurrcsgdzutwgjofowhryrubn", "hudqbfnzxnvpluwicurr", "xaezuqlsfvchjf",
                        "tvibbwxnokzkhndmdhweyeycamjeplec", "olnswlvtlbmkrsurrcsgdzu",
                        "qiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyyt", "eiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwyl",
                        "cgiowuuudrgzmwnxaezuqlsfvchjflocz", "rxric", "cygycdpehteiugqbptyqbvokpwovbnplshnzaf", "g",
                        "surrcsgd", "yzenflfnhrptuugyfsghluythksqh", "gdzutwgjofowhryrubnxkahocqjzwwagqid",
                        "ddeoincygycdpeh", "yznmojdhbeomyjqptltpugzceyzenflfnhrptuug", "ejuisks",
                        "teiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoi", "mrwnxhaqfezeeabuacyswollycgio",
                        "qfskkpfakjretogrokmxemjjbvgmmqrfdxlkfvycwalbdeumav",
                        "wjgjhlrpvhqozvvkifhftnfqcfjmmzhtxsoqbeduqmnpvimagq",
                        "ibxhtobuolmllbasaxlanjgalgmbjuxmqpadllryaobcucdeqc",
                        "ydlddogzvzttizzzjohfsenatvbpngarutztgdqczkzoenbxzv",
                        "rmsakibpprdrttycxglfgtjlifznnnlkgjqseguijfctrcahbb",
                        "pqquuarnoybphojyoyizhuyjfgwdlzcmkdbdqzatgmabhnpuyh",
                        "akposmzwykwrenlcrqwrrvsfqxzohrramdajwzlseguupjfzvd",
                        "vyldyqpvmnoemzeyxslcoysqfpvvotenkmehqvopynllvwhxzr",
                        "ysyskgrbolixwmffygycvgewxqnxvjsfefpmxrtsqsvpowoctw",
                        "oqjgumitldivceezxgoiwjgozfqcnkergctffspdxdbnmvjago",
                        "bpfgqhlkvevfazcmpdqakonkudniuobhqzypqlyocjdngltywn",
                        "ttucplgotbiceepzfxdebvluioeeitzmesmoxliuwqsftfmvlg",
                        "xhkklcwblyjmdyhfscmeffmmerxdioseybombzxjatkkltrvzq",
                        "qkvvbrgbzzfhzizulssaxupyqwniqradvkjivedckjrinrlxgi",
                        "itjudnlqncbspswkbcwldkwujlshwsgziontsobirsvskmjbrq",
                        "nmfgxfeqgqefxqivxtdrxeelsucufkhivijmzgioxioosmdpwx",
                        "ihygxkykuczvyokuveuchermxceexajilpkcxjjnwmdbwnxccl",
                        "etvcfbmadfxlprevjjnojxwonnnwjnamgrfwohgyhievupsdqd",
                        "ngskodiaxeswtqvjaqyulpedaqcchcuktfjlzyvddfeblnczmh",
                        "vnmntdvhaxqltluzwwwwrbpqwahebgtmhivtkadczpzabgcjzx",
                        "yjqqdvoxxxjbrccoaqqspqlsnxcnderaewsaqpkigtiqoqopth",
                        "wdytqvztzbdzffllbxexxughdvetajclynypnzaokqizfxqrjl",
                        "yvvwkphuzosvvntckxkmvuflrubigexkivyzzaimkxvqitpixo",
                        "lkdgtxmbgsenzmrlccmsunaezbausnsszryztfhjtezssttmsr",
                        "idyybesughzyzfdiibylnkkdeatqjjqqjbertrcactapbcarzb",
                        "ujiajnirancrfdvrfardygbcnzkqsvujkhcegdfibtcuxzbpds",
                        "jjtkmalhmrknaasskjnixzwjgvusbozslrribgazdhaylaxobj",
                        "nizuzttgartfxiwcsqchizlxvvnebqdtkmghtcyzjmgyzszwgi",
                        "egtvislckyltpfogtvfbtxbsssuwvjcduxjnjuvnqyiykvmrxl",
                        "ozvzwalcvaobxbicbwjrububyxlmfcokdxcrkvuehbnokkzala",
                        "azhukctuheiwghkalboxfnuofwopsrutamthzyzlzkrlsefwcz",
                        "yhvjjzsxlescylsnvmcxzcrrzgfhbsdsvdfcykwifzjcjjbmmu",
                        "tspdebnuhrgnmhhuplbzvpkkhfpeilbwkkbgfjiuwrdmkftphk",
                        "jvnbeqzaxecwxspuxhrngmvnkvulmgobvsnqyxdplrnnwfhfqq",
                        "bcbkgwpfmmqwmzjgmflichzhrjdjxbcescfijfztpxpxvbzjch",
                        "bdrkibtxygyicjcfnzigghdekmgoybvfwshxqnjlctcdkiunob",
                        "koctqrqvfftflwsvssnokdotgtxalgegscyeotcrvyywmzescq",
                        "boigqjvosgxpsnklxdjaxtrhqlyvanuvnpldmoknmzugnubfoa",
                        "jjtxbxyazxldpnbxzgslgguvgyevyliywihuqottxuyowrwfar",
                        "zqsacrwcysmkfbpzxoaszgqqsvqglnblmxhxtjqmnectaxntvb",
                        "izcakfitdhgujdborjuhtwubqcoppsgkqtqoqyswjfldsbfcct",
                        "rroiqffqzenlerchkvmjsbmoybisjafcdzgeppyhojoggdlpzq",
                        "xwjqfobmmqomhczwufwlesolvmbtvpdxejzslxrvnijhvevxmc",
                        "ccrubahioyaxuwzloyhqyluwoknxnydbedenrccljoydfxwaxy",
                        "jjoeiuncnvixvhhynaxbkmlurwxcpukredieqlilgkupminjaj",
                        "pdbsbjnrqzrbmewmdkqqhcpzielskcazuliiatmvhcaksrusae",
                        "nizbnxpqbzsihakkadsbtgxovyuebgtzvrvbowxllkzevktkuu",
                        "hklskdbopqjwdrefpgoxaoxzevpdaiubejuaxxbrhzbamdznrr",
                        "uccnuegvmkqtagudujuildlwefbyoywypakjrhiibrxdmsspjl",
                        "awinuyoppufjxgqvcddleqdhbkmolxqyvsqprnwcoehpturicf" }));
    }
}
