# (C) 2013 - Francsico Viveros, Grigori Sidorov, SUPPORTED BY:  IPN, Conacyt, ICYT DF 
# Convert FreeLing dep format into Stanford dependency format (not collapsed), Freeling deos NOT mantain the real word order 
# Parmeters: input output 2 1 1
# Three last numbers can be 0 or 1 or 2 or 3. It shows which part of the three member we take: relationship, main word, dependent word. 
# 0 - we take both parts, 1 - the first part, 2 - the second part, 3 - the third part (3 is not applicable for relation names, they have only two parts). 
# Default is "2 1 1".
# You may want to change the separator value for the output. Default is "-", but then you should process carefully the dash "-" in the sentence.
# You may want to use "##". E.g. "espec(tiempo##8, mucho##9)" "sp-mod(tiempo##8, de##10)", etc. vs. "espec(tiempo-8, mucho-9)", "sp-mod(tiempo-8, de-10)" etc.


import sys

separator = "-"  # You may need "-" or "##"

if len(sys.argv) <= 2:
        print ("Usage with parameters: [input output 1 1 1];  or at least [input output]\n")
        sys.exit(1);

inp    = sys.argv[1]
output = sys.argv[2]
param1 = "2"
param2 = "1"
param3 = "1"

if len (sys.argv) > 3:
        param1 = sys.argv[3]
        if not (param1 == "0" or param1 == "1" or param1 == "2"):
                param1 = "2"    
if len (sys.argv) > 4:
        param2 = sys.argv[4]
        if not (param2 == "0" or param2 == "1" or param2 == "2" or param2 == "3"):
                param2 = "1"
if len (sys.argv) > 5:
        if not (param3 == "0" or param3 == "1" or param3 == "2" or param3 == "3"):
                param3 = "1"    
        param3 = sys.argv[5]
 
fout   = open(output,"w")
f      = open(inp,   "r")

nivel         = 0
nivelanterior = -1
palabra       = 1

lista = []

for line in f:
        line = line.lower()
        if line.strip () != "":
                if line.strip () == "]":
                        if len(lista) > 0:
                                lista.pop ()                                
                else:
                        nivel     = len (line) - len (line.lstrip())
                        relation  = line [ : line.find("/(")].strip()
                        full_node = line [line.find("/(") + 2 : line.find(" -)")].strip().replace(" ","/")

                        if   param1 == "1" :
                                relation = relation [ : relation.find("/") - 1]
                        elif param1 == "2":
                                relation = relation [relation.find("/") + 1 : ]
                                
                        dep_node = full_node;
                        if   param3 == "1" :
                                dep_node = dep_node [ : dep_node.find("/")]
                        elif param3 == "2" :
                                dep_node = dep_node [dep_node.find("/") + 1 : dep_node.rfind("/") ]
                        elif param3 == "3" :
                                dep_node = dep_node [dep_node.rfind("/") : ]

                        if dep_node == "":
                                dep_node = "/"
                        
                        # Separator between word and its position is "separator", e.g., it can be "-" or "##"
                        if nivel == 0:    # New sentence
                                nivel         = 0
                                nivelanterior = -1
                                palabra       = 1
                                dep_node = dep_node + separator + str(palabra)                                

                                root_rel = "root"
                                if param1 == "0":
                                        root_rel = "root/root"
                                root_dep = "root"
                                if param2 == "0":
                                        root_dep = "root/root/root"
                                root_main = "root"
                                if param3 == "0":
                                        root_main = "root/root/root"
                                
                                #fout.write(root_rel + "(" + root_main.upper() + separator + "0, " + root_dep + separator + "0)\n")   # it can be removed, it is empty adding for compatibility
                                fout.write(relation + "(" + root_main         + separator + "0, " + dep_node +   ")\n")
                        else:
                                dep_node = dep_node + separator + str(palabra)
                                main_node = lista [len(lista) - 1] [0]   # The word info like "tables/table/N" from the tuple
                                if   param2 == "1" :
                                        main_node = main_node [ : main_node.find("/")]
                                elif param2 == "2" :
                                        main_node = main_node [main_node.find("/") + 1 : main_node.rfind("/") ]
                                elif param2 == "3" :
                                        main_node = main_node [main_node.rfind("/") : ]

                                if main_node == "":
                                        main_node = "/"
                                main_node = main_node + separator + str(lista [len(lista) - 1] [1])  # Word number from the tuple
                                
                                fout.write(relation + "(" + main_node + ", " + dep_node + ")\n")

                        if line.strip().endswith ("["):
                                tpl = (full_node, palabra)
                                lista.append ( tpl )         # We save the tuple                               

                        palabra       = palabra + 1
                        nivelanterior = nivel
        else:
                fout.write("\n")

f.close();
fout.close();