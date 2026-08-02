

int distanceBetweenBusStops(int* distance, int distanceSize, int start, int destination){
    

    if (start > destination) {
        int temp = start;
        start = destination;
        destination = temp;
    }

    int total = 0;
    int path = 0;

    for (int i = 0; i < distanceSize; i++) {
        total += distance[i];

        if (i >= start && i < destination)
            path += distance[i];
    }

    return (path < total - path) ? path : total - path;
}

