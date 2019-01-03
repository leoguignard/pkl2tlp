#!/usr/bin/env/python

import argparse
import cPickle as pkl

def write_tlp_from_lin_tree(name, lin_tree_information, lin_name, ListProperties=[]):
    """
    Write a lineage tree into an understable tulip file
    name : path to the tulip file to create
    lin_tree : lineage tree to write
    properties : dictionary of properties { 'Property name': [{c_id: prop_val}, default_val]}
    """
    
    lin_tree=lin_tree_information[lin_name]
    if ListProperties is None:
        ListProperties=['volumes_information','h_mins_information','sigmas_information']
    properties=[] #Properties Dictionary initialisation
    for l in ListProperties:
        if l is not 'Names':
            properties.append((l,lin_tree_information[l],sum(lin_tree_information[l].values())/float(len(lin_tree_information[l]))))


    nodes=set(lin_tree.keys()).union(set([v for values in lin_tree.values() for v in values]))

    f=open(name, "w")
    inv_lin_tree={v:k for k, vals in lin_tree.iteritems() for v in vals}
    f.write("(tlp \"2.0\"\n")
    f.write("(nodes ")
    for n in nodes:
        f.write(str(n)+ " ")
    f.write(")\n")


    nodes=set(lin_tree.keys()).union(set([v for values in lin_tree.values() for v in values]))
    count_edges=0
    for m, ds in lin_tree.iteritems():
        count_edges+=1
        for d in ds:
            f.write("(edge " + str(count_edges) + " " + str(m) + " " + str(d) + ")\n")
    f.write("(property 0 int \"id\"\n")
    f.write("\t(default \"0\" \"0\")\n")
    for node in nodes:
        f.write("\t(node " + str(node) + str(" \"") + str(node) + "\")\n")
    f.write(")\n")

    for property in properties:
        prop_name=property[0]
        vals=property[1]
        default=property[2]
        f.write("(property 0 string \""+prop_name+"\"\n")
        f.write("\t(default \""+str(default)+"\" \"0\")\n")
        for node in nodes:
            f.write("\t(node " + str(node) + str(" \"") + str(vals.get(node, default)) + "\")\n")
        f.write(")\n") 
    f.write(")")
    f.close()


def main():
    parser = argparse.ArgumentParser(description='Convert pkl lineage into tulip lineage.')
    parser.add_argument('-i', '--input', help='input pickle .pkl file', required=True)
    parser.add_argument('-o', '--output', help='output tulip file (has to end with .tlp)', required=True)
    
    args = parser.parse_args()
    with open(args.input) as f:
        DATA = pkl.load(f)

    if 'lin_tree' in DATA.keys():
        lin_name = 'lin_tree'
    elif 'Lineage tree' in DATA.keys():
        lin_name = 'Lineage tree'
    else:
        print "There is no known key value for the lineage tree (expected 'lin_tree' or 'Lineage tree').\n\n\tThe script will not output a tulip file."
        exit
    write_tlp_from_lin_tree(args.output, DATA, lin_name)


if __name__ == '__main__':
    main()
