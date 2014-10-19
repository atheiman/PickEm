var weekStartDates = [
	new Date('Apr 1 2014'),   	// wk 1 - Sun Sep 7
	new Date('Sep 10 2014'),   	// wk 2 - Sun Sep 14
	new Date('Sep 17 2014'),   	// wk 3 - Sun Sep 21
	new Date('Sep 24 2014'),   	// wk 4 - Sun Sep 28
	new Date('Oct 1 2014'),   	// wk 5 - Sun Oct 5
	new Date('Oct 8 2014'),   	// wk 6 - Sun Oct 12
	new Date('Oct 15 2014'),   	// wk 7 - Sun Oct 19
	new Date('Oct 22 2014'),   	// wk 8 - Sun Oct 26
	new Date('Oct 29 2014'),   	// wk 9 - Sun Nov 2
	new Date('Nov 5 2014'),   	// wk 10 - Sun Nov 9
	new Date('Nov 12 2014'),   	// wk 11 - Sun Nov 16
	new Date('Nov 19 2014'),   	// wk 12 - Sun Nov 23
	new Date('Nov 26 2014'),   	// wk 13 - Sun Nov 30
	new Date('Dec 3 2014'),   	// wk 14 - Sun Dec 7
	new Date('Dec 10 2014'),   	// wk 15 - Sun Dec 14
	new Date('Dec 17 2014'),   	// wk 16 - Sun Dec 21
	new Date('Dec 24 2014'),   	// wk 17 - Sun Dec 28
	new Date('Dec 31 2014'),   	// Wild Card - Sat, Sun Jan 3, 4
	new Date('Jan 7 2014'),   	// Divisional - Sat, Sun Jan 10, 11
	new Date('Jan 14 2014'),   	// Championship - Sun Jan 18
	                        	// Pro Bowl - Sun Jan 25
	new Date('Jan 21 2014')   	// Super Bowl - Sun Feb 1
]

function getWeekStartDate(weekNumber, weekStartDatesArray) {
	// getWeekStartDate(4) returns the wed before week 4.
	// getWeekStartDate(18) returns the wed before the wild card round.
	// getWeekStartDate(19) returns the wed before the divisional round.
	// getWeekStartDate(20) returns the wed before the championship round.
	// getWeekStartDate(21) returns the wed before the pro bowl round.
	// getWeekStartDate(22) returns the wed before the super bowl round.
	weekStartDatesArray = weekStartDatesArray || weekStartDates;
	var index = weekNumber - 1;
	return weekStartDatesArray[index];
}

function getCurrentWeek(nowDate, weekStartDatesArray) {
	nowDate = nowDate || new Date();
	weekStartDatesArray = weekStartDatesArray || weekStartDates;
	for (var week = 1; week < 23; week++) {
		// if (nowDate < getWeekStartDate(week)) {
		// 	var currentWeek = week;
		// 	break;
		// } else {
		// 	var currentWeek = 22
		// }
		if ( nowDate > getWeekStartDate(week) && nowDate < getWeekStartDate(week + 1)) {
			var currentWeek = week;
		} else if (nowDate < getWeekStartDate(1)) {
			var currentWeek = 1;
		} else if (nowDate > getWeekStartDate(22)) {
			var currentWeek = 22
		}
	}
	return currentWeek;
}

function pick(picksetId, gameId, pick, abbreviation, correct) {
    this.picksetId = picksetId;
    this.gameId = gameId;
    this.pick = pick;
    this.abbreviation = abbreviation;
    switch(correct) {
		case 'False':
			this.correct = false;
			break;
		case 'True':
			this.correct = true;
			break;
		default:
			this.correct = null;
	}
}

function selectPick(gameId, pick) {
	element = document.forms["pickForm"]['game' + gameId].value = pick;
}

// function highlightCurrentWeek(weeksNavElement) {
// 	weeksNavElement = weeksNavElement || document.getElementById('weeks');
// 	if (weeksNavElement.tagName === "NAV") {
// 		var currentWeek = getCurrentWeek();
// 		for (var n in weeksNavElement.childNodes) {
// 			var node = weeksNavElement.childNodes[n];
// 			if (node.tagName === "A") {
// 				if (node.innerHTML == currentWeek) {
// 					node.className = "bold large";
// 				}
// 			}
// 		}
// 	}
// }

// function highlightSelectedWeek(weeksNavElement) {
// 	weeksNavElement = weeksNavElement || document.getElementById('weeks');
// 	if (weeksNavElement.tagName === "NAV") {
// 		var pathArray = window.location.pathname.split('/');
// 		var selectedWeek = pathArray[pathArray.length - 1];
// 		for (var n in weeksNavElement.childNodes) {
// 			var node = weeksNavElement.childNodes[n];
// 			if (node.tagName === "A") {
// 				if (node.innerHTML == selectedWeek) {
// 					node.className = "bold large";
// 				}
// 			}
// 		}
// 	}
// }

function highlightCurrentAndSelectedWeek(weeksNavElement) {
	weeksNavElement = weeksNavElement || document.getElementById('weeks');
	if (weeksNavElement.tagName === "NAV") {
		var currentWeek = getCurrentWeek();
		var pathArray = window.location.pathname.split('/');
		var selectedWeek = pathArray[pathArray.length - 1];
		for (var n in weeksNavElement.childNodes) {
			var node = weeksNavElement.childNodes[n];
			if (node.tagName === "A") {
				if (node.innerHTML == selectedWeek || node.innerHTML == currentWeek) {
					node.className = "bold large";
				}
			}
		}
	}
}

function formatSpreads(spreadSpans) {
	spreadSpans = spreadSpans || document.getElementsByClassName('gameSpread');
	for (var s in spreadSpans) {
		// console.log(typeof(spreadSpans[g].innerHTML));
		if (spreadSpans[s].innerHTML) {
			var spread = spreadSpans[s];
			if (spread.innerHTML === "0.0") {
				spread.innerHTML = "0";
			}
			if (/^\d+/.test(spread.innerHTML)) {
				spread.innerHTML = "+" + spread.innerHTML;
			}
		}
	}
}
