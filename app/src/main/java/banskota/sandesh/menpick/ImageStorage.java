package banskota.sandesh.menpick;

import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import java.io.File;

/**
 * Created by Winston on 3/24/2018.
 */

public class ImageStorage extends AppCompatActivity
{
	private FirebaseStorage storage;
	private StorageReference storageRef;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);

		storage = FirebaseStorage.getInstance();
		storageRef = storage.getReference();

		Uri file = Uri.fromFile(new File("path/to/RANDOM_FILE"));
		StorageReference tempRef = storageRef.child("menus/" + file.getLastPathSegment());
		UploadTask uploadTask = tempRef.putFile(file);

		// Register observers to listen for when the download is done or if it fails
		uploadTask.addOnFailureListener(new OnFailureListener() {
			@Override
			public void onFailure(@NonNull Exception exception) {
				// Handle unsuccessful uploads
			}
		}).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
			@Override
			public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
				// taskSnapshot.getMetadata() contains file metadata such as size, content-type, and download URL.
				Uri downloadUrl = taskSnapshot.getDownloadUrl();
			}
		});
	}
}
