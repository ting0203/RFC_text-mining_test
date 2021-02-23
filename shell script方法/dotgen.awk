BEGIN {
	printf("digraph BGP_RFCs {\nrankdir = \"LR\";\n");
}
END {
	for (i in year) {
		printf("\tsubgraph YEAR%s { rank = same; \"%s\" [ shape=box ]; %s }\n", i, i, year[i]);
	}
	for (i in year) {
		printf("\"%s\" -> ", i);
	}
	printf("\"\";\n}\n");
}
{
	ii = 3;
	fillcolor = "white";
	if ($ii == "Obsoleted-By") {
		fillcolor = "red";
		ii++;
		while (ii<=NF) {
			if ($ii == "Updated-By") break;
			printf("\tRFC%s -> RFC%s [color = red];\n", $1, $ii);
			ii++;
		}
	}
	if ($ii == "Updated-By") {
		ii++;
		while (ii<=NF) {
			printf("\tRFC%s -> RFC%s [color = blue];\n", $1, $ii);
			ii++;
		}
	}
	printf("\tRFC%s [shape=%s, style=filled, fillcolor=%s, label=\"%s\"];\n", $1, "box", fillcolor, $1);
	year[$2] = year[$2] " RFC" $1 ";";
}
