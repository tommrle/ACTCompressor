# this encodes the string produced by the LZ77 compressor with the huffman encoding produced by Aaron

import json
from pprint import pprint
from dataImport import SymFreq
import pickle




def encode(stringAfterLZ77, fileName):
    tempFile = open(fileName)
    huffTree = json.load(tempFile)
    tempFile.close()

    encoded = ""
    i = 0
    while i < len(stringAfterLZ77):
        currentChar = stringAfterLZ77[i]
        if currentChar == "[" or currentChar == "]":
            j = i
            ended = False
            i += 1
            while not ended:
                if stringAfterLZ77[i] == "]":
                    ended = True
                i += 1
            encoded += "1"+encodePair(stringAfterLZ77[j+1:i-1])
        else:
            encoded += "0"
            encoded += huffTree[currentChar]
            i += 1
    #print (encoded)
    return encoded


def encodePair(pair):
    i = 0
    while pair[i] != ",":
        i += 1
    length = int(pair[:i])
    i += 1
    dist = int(pair[i:])

    prev = 0
    bits = 0
    if length == 3:
        result = '00000'
    elif length == 4:
        result = '00001'
    elif length == 5:
        result = '00010'
    elif length == 6:
        result = '00011'
    elif length == 7:
        result = '00100'
    elif length == 8:
        result = '00101'
    elif length == 9:
        result = '00110'
    elif length == 10:
        result = '00111'
    elif length <= 12:
        result = '01000' + bin(length - 11)[2:]
        prev = 11
        bits = 1
    elif length <= 14:
        result = '01001' + bin(length - 13)[2:]
        prev = 13
        bits = 1
    elif length <= 16:
        result = '01010' + bin(length - 15)[2:]
        prev = 15
        bits = 1
    elif length <= 18:
        result = '01011' + bin(length - 17)[2:]
        prev = 17
        bits = 1
    elif length <= 22:
        result = '01100' + bin(length - 19)[2:]
        prev = 19
        bits = 2
    elif length <= 26:
        result = '01101' + bin(length - 23)[2:]
        prev = 23
        bits = 2
    elif length <= 30:
        result = '01110' + bin(length - 27)[2:]
        prev = 27
        bits = 2
    elif length <= 34:
        result = '01111' + bin(length - 31)[2:]
        prev = 31
        bits = 2
    elif length <= 42:
        result = '10000' + bin(length - 35)[2:]
        prev = 35
        bits = 3
    elif length <= 50:
        result = '10001' + bin(length - 43)[2:]
        prev = 43
        bits = 3
    elif length <= 58:
        result = '10010' + bin(length - 51)[2:]
        prev = 51
        bits = 3
    elif length <= 66:
        result = '10011' + bin(length - 59)[2:]
        prev = 59
        bits = 3
    elif length <= 82:
        result = '10100' + bin(length - 67)[2:]
        prev = 67
        bits = 4
    elif length <= 98:
        result = '10101' + bin(length - 83)[2:]
        prev = 83
        bits = 4
    elif length <= 114:
        result = '10110' + bin(length - 99)[2:]
        prev = 99
        bits = 4
    elif length <= 130:
        result = '10111' + bin(length - 115)[2:]
        prev = 115
        bits = 4
    elif length <= 162:
        result = '11000' + bin(length - 131)[2:]
        prev = 131
        bits = 5
    elif length <= 194:
        result = '11001' + bin(length - 163)[2:]
        prev = 163
        bits = 5
    elif length <= 226:
        result = '11010' + bin(length - 195)[2:]
        prev = 195
        bits = 5
    elif length <= 257:
        result = '11011' + bin(length - 227)[2:]
        prev = 227
        bits = 5
    else:
        result = '11100'

    if bits > 0:
        post = bin(length - prev)[2:]
        while len(post) < bits:
            post = '0' + post
        result += post

    prev = 0
    bits = 0
    if dist == 1:
        result += '00000'
    elif dist == 2:
        result += '00001'
    elif dist == 3:
        result += '00010'
    elif dist == 4:
        result += '00011'
    elif dist <= 6:
        result += '00100'
        prev = 5
        bits = 1
    elif dist <= 8:
        result += '00101'
        prev = 7
        bits = 2
    elif dist <= 12:
        result += '00110'
        prev = 9
        bits = 2
    elif dist <= 16:
        result += '00111'
        prev = 13
        bits = 2
    elif dist <= 24:
        result += '01000'
        prev = 17
        bits = 3
    elif dist <= 32:
        result += '01001'
        prev = 25
        bits = 3
    elif dist <= 48:
        result += '01010'
        prev = 33
        bits = 4
    elif dist <= 64:
        result += '01011'
        prev = 49
        bits = 4
    elif dist <= 96:
        result += '01100'
        prev = 65
        bits = 5
    elif dist <= 128:
        result += '01101'
        prev = 97
        bits = 5
    elif dist <= 192:
        result += '01110'
        prev = 129
        bits = 6
    elif dist <= 256:
        result += '01111'
        prev = 193
        bits = 6
    elif dist <= 384:
        result += '10000'
        prev = 257
        bits = 7
    elif dist <= 512:
        result += '10001'
        prev = 384
        bits = 7
    elif dist <= 768:
        result += '10010'
        prev = 513
        bits = 8
    elif dist <= 1024:
        result += '10011'
        prev = 169
        bits = 8
    elif dist <= 1536:
        result += '10100'
        prev = 1025
        bits = 9
    elif dist <= 2048:
        result += '10101'
        prev = 1537
        bits = 9
    elif dist <= 3072:
        result += '10110'
        prev = 2049
        bits = 10
    elif dist <= 4096:
        result += '10111'
        prev = 3073
        bits = 10
    elif dist <= 6144:
        result += '11000'
        prev = 4097
        bits = 11
    elif dist <= 8192:
        result += '11001'
        prev = 6145
        bits = 11
    elif dist <= 12288:
        result += '11010'
        prev = 8193
        bits = 12
    elif dist <= 16384:
        result += '11011'
        prev = 12289
        bits = 12
    elif dist <= 24576:
        result += '11100'
        prev = 16385
        bits = 13
    else:
        result += '11101'
        prev = 24577
        bits = 13

    if dist >= 6:
        post = bin(dist - prev)[2:]
        while len(post) < bits:
            post = '0' + post
        result += post
    return result

# print huffTree
#
input="engaged in a back and forth Sunday wi[12,3]the parents of[44,3]dead American soldier  extending[72,3] argum[51,3] between[70,5]Republ[54,5]presid[84,3]ial [71,3]didate[130,5]Muslim immigra[118,4]who were l[87,3]ely unknown[8,3]til[161,4]y appe[165,3]d at[178,5]Democratic N[6,3]on[104,3]Conv[199,3]io[143,4]ree [228,3]s ago   I[180,3]n interview [36,3]ABC s  This Week[38,3]M[232,3]Trump took issue with Khizr[6,3]an [176,5]had ques[123,4]ed[195,3]e[167,3]r[65,11]h[33,3]re[38,3]t[174,3]U S [159,4]stitu[174,4] and said[115,11]h[83,3] sacrific[234,3]nothing[189,3]M[151,9]respond[114,3]by cit[32,4]h[192,3]har[133,3]ork[230,3]d business succ[8,4]   I ve c[146,3]t[175,3]thous[131,3]s[136,5]t[14,9]of job[48,3]ten[14,5]t[41,9]o[27,8]built g[220,3]t structu[150,3] [166,12]told host George Stephanopoulo[143,4]I[131,3]ink[137,3]ey[213,3] [247,9]s[170,4]t[248,3]k  when[184,3]can employ[184,17]o[198,7]of people[186,3]ak[232,3]a[84,3]o[191,4]eir education[216,3]a[30,11]so man[86,4]ing[245,3] [196,12]al[31,3]note[202,3]is ro[93,3]in help[46,3] bui[228,3]a Vietnam Memorial[36,4]Manhatt[183,3] [235,3] [239,3] [243,3]  Khizr[6,3]a[137,3]whos[247,3]o[148,3]Army Capt  Humayun[42,3]an was kill[130,3]in Iraq[129,4] [168,5]offer[155,3]bit[188,3] cr[8,3]cism[245,4]Dona[156,3]T[199,6]t[223,3]e DNC  ask[233,3]  Have you even read[36,5]Uni[238,4]States Constituti[164,4] Photo  Getty Imag[35,3]Bu[93,6]Republic[241,3]nominee immedi[73,3]ly ig[89,6]ano[139,3]r furor by say[189,4]Mr [241,6]s wife[101,3]hazala  h[154,3]be[164,3] extrem[78,4]quiet  [158,4]age[224,9]emocratic con[215,3]t[183,4]and perhaps s[226,3] wasn t allow[235,3]to[99,3]v[69,3]nyth[139,4]to[149,4]   T[215,3]K[148,3]s[165,4] [60,4]was[48,3]o distraugh[252,3]o speak about [220,4]s[118,3]s[64,3]   death[75,3] E[143,3] before[172,4]y we[10,3]air[130,3]in full[207,3] Sund[124,3]morn[139,4] [215,4]comm[204,3]s gene[223,3]ed[223,4]trovers[168,3]Mr[171,3]rump[117,3]aggressi[208,3] attack[210,4]style kep[160,3]im[25,3] [131,3] [140,4]fr[74,3] of[148,4] new[223,3]hro[217,3]o[204,3]t[256,3]Republican primarie[102,3]s[232,3] knock[191,3]off[237,4]rival[247,3]he is now try[197,4]t[196,3]sam[5,3]t[190,4]g[252,3]ith a much broade[195,3]m[14,4]m[148,3] d[191,3]rse electo[242,4]  [137,3]spond[207,4]to[192,5]criticism  M[64,3]Trump[123,3]su[148,3]a[244,3]ateme[222,3]l[117,3] Saturday call[150,4]Capt  Humay[220,3]Kh[225,3] Khizr s so[13,3]a[203,4]ro[219,3]and[193,3]y[204,8] real proble[124,3]i[244,3]radi[89,3] Islamic terrorist[28,3]   While I feel deeply for[198,5]loss of h[72,3]s[120,4]M[204,3]K[143,4]who has never met[4,3] [18,6]o right to[232,4]nd in fro[237,3]of mi[226,3]on[86,5]peop[123,3]a[194,3]claim[133,3]have[84,7]read[211,5]C[47,3]titut[56,3]  [122,3]ich[217,4]fals[241,3]a[98,3]say many o[182,3]r[113,3]accurate[198,3]ing[233,4]M[186,3]Trump[45,3]i[148,5]t[225,3]st[37,3]me[156,3] [220,10]responded emo[118,4]ally[207,4]M[254,3]T[68,5]aga[214,3]on Sund[125,3] [130,3]ing [175,3]appreci[125,3]s[191,5]c[224,3]id[140,4]s[212,3]cogni[202,5]of h[198,3]s[213,3]as a[59,3]ro but[244,3]at[27,5]ide[26,3]rem[108,4]un Ameri[79,3] [205,11]h[60,3]c[160,3]ed for[71,3]b[193,3]on Muslims [219,3]er[154,4]t[238,3]U S[232,3]or[254,4]o[255,3]r vers[225,3]s[142,4]t[189,3]proposal [145,3]b[106,3]on immigra[180,5]from countri[223,3]com[49,3]mis[126,3]by [106,3]rorism[101,3] H[220,3]polic[41,4] [234,4]practic[56,3] do not[219,3]flec[242,8]e[205,5]any[236,3]d[152,3]tand[186,4]o[155,6]basic  f[29,3]am[215,3]al[138,3]nstitu[156,4]al[189,3]incipl[154,3]o[207,4]i[162,4]u[172,3]y  w[99,4]mak[182,3]t[141,4]c[197,5]y excep[220,4]al in[138,3]e[172,4]to[52,3]of[49,3]nkind[208,3]Mr  Khan said on CNN [217,3]State[163,8]Un[137,3] [254,3]He choked up [213,3]he[236,3]spo[216,3]d to[78,5]Trump[67,3]insinua[196,4] t[166,4]h[184,3]wif[137,3]a[45,5]rema[155,3]sil[246,3] [243,4]age  Ghazala[150,6]becom[248,4]verwhelm[123,3]whe[175,3]he se[246,3]her s[184,3]s pictur[66,3]which w[160,3]project[176,3]i[133,4]e conv[110,3]i[233,3]hall [194,4]s[250,4]  In a[32,3]lumn[188,3] T[248,3]Washingt[253,3]Pos[164,4] Sunday [234,3]s [163,6]respond[153,3]to[23,3]  Trump[144,3]ques[254,4]ing[180,3]y[179,5]did[137,3] speak[116,3]Withou[16,3]ay[104,3] a[164,3]i[46,3] [155,4]t[226,3]worl[156,3]a[170,3]America  felt my pa[212,3] [86,5]wrot[248,3] I am[197,3]Go[53,3]Star mo[245,3]r[104,3]hoev[9,3]saw me[67,7]e[231,4]their heart[144,3] S[246,3]said it was[172,4]true[152,3]a[182,3]h[146,3]a[21,5]allow[243,6]s[204,5]a[41,3]he conven[246,4] [213,8]h[129,3]husband had ask[57,3]if[186,6]ant[71,6] bu[98,6]f[224,4]o[174,3]whelm[100,3] [192,3]alk[76,4]on[113,3]t[242,3]c[104,10]stag[253,3]with[252,3]hu[13,3]picture of my s[141,3]behi[128,3]m[41,3]I[165,3]ul[140,4]rdly[178,4]trol[41,3]self[107,3]h[234,3]mo[205,3]r[206,3]u[41,3] [249,6]rot[103,3] Dona[62,3]Trump[208,3]s children whom[238,3] l[189,3]s[41,4]es[253,3] real[104,3]ne[246,3]to wond[91,3]why[138,3]did no[248,3]peak[233,4]Mr  Khan in his[61,3]marks[249,3] Sunda[206,3]a[52,3] two t[211,3]gs a[233,3]absolute[208,3]necessari[220,3]in any lea[115,4]or[14,5]pers[79,3]t[232,4]aspir[173,4]t[246,4]wi[233,3]s[93,3]o b[84,3] [56,7] a moral compas[219,3]and sec[202,3] [164,3]e[22,3]t[207,3] [193,3]T[181,4]c[32,3]idate[30,4]vo[228,3]of both traits[186,3]a[124,3]re[173,9]y f[158,3]stewardship[50,4]t[76,5]ount[32,3]  he[252,6]in [101,4]remarks [203,3] St[109,4]o[51,4]e Uni[223,3]   Democratic p[229,3]identi[199,4]a[159,8]Hill[125,4]Clint[73,3]s[96,7]Clevel[230,4]t[170,4]Mr[217,3]rump wa[113,3]ffering a divisive m[198,4]ge[166,3] [45,4]Khan p[173,4]t[182,3]ultim[161,4]sacrifice[196,8]famil[220,3]didn t[226,4]  s[232,8]  A[129,3]w[129,4]h[119,3]he[32,3]ard from Donald[150,7] Noth[146,4]but[191,3]s[113,3]s[85,3]egrad[169,4]comm[252,3]s abo[34,3]Muslim[34,3]a total misunderst[243,3]i[218,3]of[120,6]made our[66,3]untry gre[143,3]religiou[193,3]reed[143,3] [19,10]libert[213,3]  Mr  Khan also called on Senate Majori[43,3]Le[104,3]r Mitch McConnell  R[69,3]K[74,4]and H[112,3]e Speak[44,3]Paul Ry[92,3] [38,4]Wisc[114,3]to withdraw their endorse[255,6]fr[171,3]the Republic[155,3]nominee[175,4]I address[60,4] [165,7]m[165,8]l[165,6]a patriot[149,5]I[51,13]s[157,7]of[126,4] [178,6] [48,7]ic Amer[117,5] It i[103,5]ir moral o[144,3]gatio[210,3]history[204,3]ll[161,3]t forgive[212,4]m[238,3]Mr  Kh[252,3]said[254,3]T[49,3] elec[63,5]w[54,4]pa[199,3] but[77,14]be w[206,3]te[132,3]T[229,3]lap[163,3]of[133,7]courag[36,3]i[121,3]be[237,3]burd[45,3]on[225,4]ir soul[89,3]  In[30,3]statement Sunday[247,3]at did[47,3] [24,4]i[207,3]M[174,3]Trump[185,6]McConne[218,3]called Capt[208,7]a[253,3]Americ[221,3]hero [19,3]d[41,8]a trave[198,3]a[146,5]Muslim[231,3]simply[190,3]n[33,3]r[134,3]o[70,10]value[178,5]AshLee Strong[89,3] spokeswom[122,3]for[169,5]Ry[135,3] reiter[220,3]d[247,4] speake[253,3] opposi[215,5]to[218,11]s pro[27,3]ed[150,7] immig[67,3]i[169,3]b[219,3]  T[74,11]has made clear[11,3]n[182,3]im[169,3]that[251,3] reject[16,4]is idea and h[240,3]elf[64,5]talk[161,3]abou[50,3]ow[122,8]A[251,7]s[102,3]ve[103,6]t[198,3]ul[98,3]at[207,3]acrifice[246,5]t[97,4]country[166,3]s[240,4]aid[177,3]M[223,9]respond[222,3]on Twitt[196,3]on Sunday morning[61,3]ay[8,4]he w[225,3] vicio[149,3]y attac[174,4] by[88,5]Khan[22,3] [153,4]conventi[92,3] [190,3] I not allow[224,3]to[127,8]  Hilla[167,3]vot[250,3]f[190,5]e Iraq[113,3]r [56,5]me[198,3]h[230,4]i[197,14]h[147,3]s[218,4]h[159,6]oppos[211,3]to[134,5]I[70,4]W[70,3]when it star[103,4] bu[168,5]re i[66,3]o[97,3]evidence[234,4]su[72,3]r[144,4]i[181,3]t[210,5]ti[134,5]T[221,3]discom[171,3]t of[62,6]Republicans with[164,11]s[236,7]s[163,6]e[104,5]t  Ohio Gov  John Kasich [171,3]o ran against[237,11]for[214,5]R[108,9] nomination  twee[220,5] [164,3]r[197,3] only[5,3]e[120,3]y to talk abo[252,3]Gold Star par[143,3]s[121,3]i[183,3]hon[102,3]and[181,5]ec[168,3]Cap[174,3]Kh[148,3]is a [93,3]o[220,3]oge[141,3]r[177,3]e shou[80,3]pr[104,3]f[166,3]h[41,3]fami[127,3]   B[112,3]Se[162,3]Jeff[10,3]ss[176,3]s  R[171,3]Ala[177,3] a[227,7]support[87,4]defend[208,3]t[243,17]inee[221,3] [193,4]t[10,3]f[36,5]Un[87,3]   saying M[155,3]T[85,5]hadn t spok[134,3]inappropri[60,3]l[161,4]H[215,3]in[117,3]view was[100,3]t unkind  it[19,5]respectful[19,5]did exp[22,3]s condolences to[176,5]f[253,6]for[191,4]ir lo[41,3] [149,5]S[52,3]ions[169,3]i[96,3] Mr[26,3]Cl[130,3]o[167,3]ook a[47,3]w key [171,5]ach Sunday[189,3] [137,4]ond[227,4]to criticism from Pat Smith [135,5]mo[141,3]r of an Americ[9,3]killed[243,3] [171,4] [151,3] attack[95,4]Benghazi  Libya  while[185,3]s[165,10]was[198,3]cretary[94,4]Stat[74,3]who d[215,6]at[249,4] Republ[118,5]convent[250,3]   I blame H[139,3]a[68,3]C[255,7]personally for[196,5]dea[207,3]of my [28,3] [177,3]M[141,12]respond[209,3]on Fox New[159,3]unday[221,3]I [10,3]erstand[240,5]grief [14,8]in[199,3]dib[227,3]sense[206,4]los[237,3] adding[199,3]at s[204,3]had no  [179,3] fee[178,3]g  toward M[145,3]Smith "
lenIn=len(input)
lenOut=len(encode(input,'../dataImport/data.json'))
print "\n"+str(lenIn*8)+" to "+str(lenOut)

pkl_file = open('../dataImport/tree.pkl', 'rb')

symbolFrequencyList = pickle.load(pkl_file)

pkl_file.close()
print symbolFrequencyList
