var weekStartDates = [new Date('Apr 1, 2014'), new Date('Sep 10, 2014')]

for (var i = 2; i <= 21; i++) {
	weekStartDates[i] = new Date();
	weekStartDates[i].setDate(weekStartDates[1].getDate()+7*(i-1));
}

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
