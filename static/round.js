// To initialize collapsible
$(document).ready(function () {
    $('.collapsible').collapsible();
});

// To initialize the map


// L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     maxZoom: 18,
//     id: 'mapbox.streets',
//     accessToken: 'pk.eyJ1Ijoicm9taXRrYXJtYWthciIsImEiOiJjandnZDB3OGwxczV4NDBtZ2l0YTJ5aGVsIn0.w0b86s6XC_CFVG726Zwjrw'
// }).addTo(mymap);

// Vue methods
var main = new Vue({
    delimiters: ['[[', ']]'],
    el: "#main",
    data: {
        round: {
            no: null,
            question: null,
            answer: null
        },
        mymap: null,
        hints: [],
        positions: [],
        hintAnswer: null
    },
    mounted() {
        var self = this;
        this.mymap = L.map('mapid').setView([51.505, -0.09], 13);

        $.getJSON("getRound").then(function (data) {
            self.round.no = data.no;
            self.round.question = data.question;
        });

        $.getJSON("getHints").then(function (data) {
            data.forEach(function (obj) { self.hints.push(obj) });
        });

        $.getJSON("getLocations").then(function (data) {
            data.forEach(function (obj) {
                var arr = obj.position.split(",");
                arr[1] = arr[1].trim();
                self.positions.push(arr)
            });
            var polygon = L.polygon(self.positions, {
                color: "red"
            }).addTo(self.mymap);
        });


    },
    methods: {
        checkHint(index, e) {
            var self = this;
            $.getJSON("checkHint?id=" + index + "&answer=" + e.target.value).then(function (data) {
                var arr = data.position.split(",");
                arr[1] = arr[1].trim();
                self.positions.push(arr);

                var polygon = L.polygon(self.positions, {
                    color: "red"
                }).addTo(self.mymap);
            });
        },
        checkRound() {
            var self = this;
            $.getJSON("checkRound?id=" + self.round.no + "&answer=" + self.round.answer).then(function(data) {
                if(data.isTrue == 1) {
                    swal("Good job!", "You gave the right answer", "success");
                } else {
                    swal("Try Again!", "You gave the wrong answer", "error");
                }
            })
        }
    }
})
