$(document).ready(function () {
    var before_item = "<span id='id_digital_competence_min_label'>do not know anything</span>";
    var after_item = "<span id='id_digital_competence_max_label'>expert level</span>";

    $("#id_digital_competence").before(before_item);
    $("#id_digital_competence").after(after_item);
});