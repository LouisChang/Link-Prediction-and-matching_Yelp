import snap
import argparse
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def getDegreeToCount(G):
    """ get (degree, count-of-node, fraction-of-node) sequences
    """
    N = G.GetNodes()
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(G, DegToCntV)
    degreeV = [ e.GetVal1() for e in DegToCntV ]
    countV = [ e.GetVal2() for e in DegToCntV ]
    normCountV = [ k / float(N) for k in countV ]
    D = {'degreeV': degreeV, 'countV': countV, 'normCountV': normCountV}
    return D

def loglog_plot(GVec, colors, labels, outfile, isLoglog = True):
    """ Log-log plot for the degree distributions
    """
    pp = PdfPages(outfile)
    plt.figure()
    plt.clf()
    
    for i in range(len(GVec)):
        G = GVec[i]  
        clr = colors[i]
        lbl = labels[i]
        D = getDegreeToCount(G)
        degreeV = D['degreeV']
        normCountV = D['normCountV']
        plt.loglog(degreeV, normCountV, color = clr, label = lbl)

    # add legend, etc
    plt.legend()
    plt.title('Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel("Fraction of Nodes")
    plt.grid()
    plt.setp(plt.gca().get_legend().get_texts(), fontsize='small')
    pp.savefig()
    pp.close()

def main(args):
    ub_review_edges_file = args.ub_review_edges
    ub_review_train_core_file = args.ub_review_train_core
    ub_review_test_core_file = args.ub_review_test_core
    degree_dist_plot_file = args.degree_dist_plot

    # load graph
    G = snap.LoadEdgeList(snap.PUNGraph, ub_review_edges_file, 0, 1)
    GTrain = snap.LoadEdgeList(snap.PUNGraph, ub_review_train_core_file, 0, 1)
    GTest = snap.LoadEdgeList(snap.PUNGraph, ub_review_test_core_file, 0, 1)

    # parameters    
    # GVec = [G, GTrain, GTest]
    GVec = [G]
    colors = ['red', 'blue', 'green']
    labels = ['All Reviews', 'Train Reviews', 'Test Reviews']

    # plot
    loglog_plot(GVec, colors, labels, degree_dist_plot_file)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process yelp data')
    parser.add_argument('--ub_review_edges', metavar='FILE', required = True, help='ub_review_edges file')
    parser.add_argument('--ub_review_train_core', metavar='FILE', required = True, help='ub_review_train_core file')
    parser.add_argument('--ub_review_test_core', metavar='FILE', required = True, help='ub_review_test_core file')
    parser.add_argument('--degree_dist_plot', metavar='FILE', required = True, help='degree_dist_plot')
    args = parser.parse_args()
    main(args)
    